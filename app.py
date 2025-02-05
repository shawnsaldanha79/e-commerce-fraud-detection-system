from flask import Flask, render_template, request
import pandas as pd
import joblib
from groq import Groq
import markdown
import csv
import os


MODEL_FILE_NAME = 'ADD_MODEL_FILE_NAME' #Eg: 'fraud_detection_model.joblib'
API_KEY = 'ADD_GROQ_API_KEY' 

app = Flask(__name__)

model = joblib.load(f"./models/{MODEL_FILE_NAME}")

client = Groq(api_key=API_KEY)

def prepare_data(form_data):
    df = pd.DataFrame([{
        'Transaction ID': form_data['transaction_id'],
        'Customer ID': form_data['customer_id'],
        'Customer Age': int(form_data['customer_age']),
        'Customer Location': form_data['customer_location'],
        'Transaction Date': form_data['transaction_date'],
        'Transaction Amount': float(form_data['transaction_amount']),
        'Product Category': form_data['product_category'],
        'Payment Method': form_data['payment_method'],
        'Shipping Address': form_data['shipping_address'],
        'Billing Address': form_data['billing_address'],
        'IP Address': form_data['ip_address'],
        'Account Age Days': int(form_data['account_age_days']),
        'Transaction Hour': int(form_data['transaction_hour']),
        'Device Used': form_data['device_used'],
        'Quantity': int(form_data['quantity'])
    }])
    df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])
    df['Transaction Day'] = df["Transaction Date"].dt.day
    df["Transaction DOW"] = df["Transaction Date"].dt.day_of_week
    df["Transaction Month"] = df["Transaction Date"].dt.month
    df["Is Address Match"] = (df["Shipping Address"] == df["Billing Address"]).astype(int)
    df.drop(columns=["Transaction ID", "Customer ID", "Customer Location",
                     "IP Address", "Transaction Date","Shipping Address",
                     "Billing Address"], inplace=True)
    return df

def get_fraud_explanation(transaction_details):
    prompt = f"""Analyze this e-commerce transaction and explain why it might be fraudulent:
    Customer Age: {transaction_details['customer_age']}
    Transaction Amount: ${transaction_details['transaction_amount']}
    Product Category: {transaction_details['product_category']}
    Payment Method: {transaction_details['payment_method']}
    Address Match: {'Yes' if transaction_details['shipping_address'] == transaction_details['billing_address'] else 'No'}
    Please provide a short explanation of potential fraud indicators in this transaction."""
    
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
        temperature=0.7,
    )
    
    return chat_completion.choices[0].message.content

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        form_data = request.form
        df = prepare_data(form_data)
        
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0]
        fraud_probability = probability[1] 
        
        explanation = None
        if prediction == 1:
            explanation = get_fraud_explanation(form_data)
            formatted_explanation = markdown.markdown(explanation)
        else:
            formatted_explanation = None
        
        transaction_data = {
            'Transaction ID': form_data['transaction_id'],
            'Customer ID': form_data['customer_id'],
            'Customer Age': form_data['customer_age'],
            'Transaction Amount': form_data['transaction_amount'],
            'Product Category': form_data['product_category'],
            'Payment Method': form_data['payment_method'],
            'Shipping Address': form_data['shipping_address'],
            'Billing Address': form_data['billing_address'],
            'IP Address': form_data['ip_address'],
            'Account Age Days': form_data['account_age_days'],
            'Transaction Hour': form_data['transaction_hour'],
            'Device Used': form_data['device_used'],
            'Quantity': form_data['quantity'],
            'Prediction': prediction,
            'Fraud Probability': fraud_probability,
            'Explanation': explanation if explanation else "None"
        }
        
        csv_file = 'transaction_predictions.csv'
        file_exists = False
        try:
            with open(csv_file, 'r'):
                file_exists = True
        except FileNotFoundError:
            pass
        with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=transaction_data.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(transaction_data)
        return render_template('result.html', 
                             prediction=prediction,
                             probability=fraud_probability,
                             transaction_details=form_data,
                             explanation=formatted_explanation)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
