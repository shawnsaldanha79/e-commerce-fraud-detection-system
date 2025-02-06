# E-Commerce Fraud Detection System

## Overview

This project is a **Fraud Detection System** for e-commerce transactions, built using **Flask, Scikit-learn, XGBoost, and Optuna**. It provides a web interface where users can input transaction details and predict whether a transaction is fraudulent.

## Features

- **Machine Learning Model:** Uses Random Forest to detect fraudulent transactions.
- **Flask Web App:** Allows users to enter transaction details and view fraud predictions.
- **AI-Powered Explanations:** Generates explanations for fraudulent predictions using Groq API.
- **Data Processing & Cleaning:** Handles missing values, categorical encoding, and feature engineering.
- **Hyperparameter Tuning:** Uses Optuna for optimizing the Random Forest model.
- **Transaction Logging:** Stores transaction results in a CSV file for auditing.

## Tech Stack

- **Backend:** Flask
- **Machine Learning:** Scikit-learn, XGBoost, Optuna
- **Database:** CSV for storing transaction predictions
- **AI Integration:** Groq API for fraud explanations

---

## Project Structure

```
├── templates/
│   ├── home.html                      # Homepage
│   ├── form.html                      # Transaction input form
│   ├── result.html                     # Fraud prediction result page
|── train_model/
|   |── fraud_prediction.ipynb         # Training code
├── app.py                              # Flask web app
├── requirements.txt                     # Python dependencies
└── README.md                            # Project documentation
```

---
## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/shawnsaldanha79/e-commerce-fraud-detection-system.git
cd e-commerce-fraud-detection-system
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the Fraud Detection Model

Run the model training script to generate a trained fraud detection model (Or you can download the model from [`here`](https://drive.google.com/uc?id=1yODGuyQFRy4E7hrgXMPKeVpNsV5nXTpQ)):

```bash
python train_model.py
```

Save the model in `/models` directory.

### 4. Run the Flask App

```bash
python app.py
```

The application will be available at **`http://localhost:5000/`**.

---

## Usage

1. **Access the Web App:** Open `http://localhost:5000/` in your browser.
2. **Enter Transaction Details:** Fill out the form with transaction information.
3. **Get Predictions:** The app will predict whether the transaction is fraudulent.
4. **AI Explanation:** If a transaction is fraudulent, the app provides an explanation.

---

## Datasets
- **Fraudulent E-Commerce Transaction Data**: This dataset contains information about e-commerce transactions, including both fraudulent and non-fraudulent labels. It features attributes such as Transaction ID, Customer ID, Transaction Amount, Transaction Date, Payment Method, Product Category, Quantity, Customer Age, Customer Location, Device Used, IP Address, Shipping Address, Billing Address, Is Fraudulent, Account Age Days, and Transaction Hour.

---

## Model Training & Evaluation

- **Data Cleaning:** Missing values handled, categorical encoding applied.
- **Feature Engineering:** Extracted features from transaction date, address match, etc.
- **ML Algorithms:** Evaluated Logistic Regression, Random Forest, Decision Tree, and XGBoost.
- **Hyperparameter Optimization:** Used Optuna to tune the best-performing model.
- **Performance Metrics:** Accuracy, Confusion Matrix, Classification Report.

---

## Results
- **Model Accuracy:** Among the models evaluated, Random Forest emerged as the most accurate, achieving a performance of 96.51% accuracy. XGBoost followed closely with an accuracy of 95.22%, and Decision Tree achieved an accuracy of 94.38%.
- **Optimized Performance:** Using Optuna for hyperparameter tuning, the Random Forest model was further optimized, improving its accuracy to 97.08%, making it the most reliable model for fraud detection.  
- **Effective Fraud Detection:** The model successfully identifies fraudulent transactions, leveraging various features such as transaction amount, product category, payment method, and customer behavior to flag anomalies.
 
---

## Dependencies

- Flask
- Pandas
- Scikit-learn
- XGBoost
- Optuna
- Joblib
- Markdown
- Groq API

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## Future Improvements

- Store predictions in a database instead of CSV.
- Implement user authentication.
- Expand fraud detection using deep learning.
- Deploy on a cloud platform (AWS/GCP/Heroku).

---

# Contributors

- Ganesh SP
- Aniruddha Nagesh Salvankar
- Shawn Glanal Saldanha
- Varun MC
