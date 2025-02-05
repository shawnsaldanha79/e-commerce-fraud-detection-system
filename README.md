# E-Commerce Fraud Detection System

## Overview

This project is a **Fraud Detection System** for e-commerce transactions, built using **Flask, Scikit-learn, Random Forest, and Optuna**. It provides a web interface where users can input transaction details and predict whether a transaction is fraudulent.

## Features

- **Machine Learning Model:** Uses Random Forest to detect fraudulent transactions.
- **Flask Web App:** Allows users to enter transaction details and view fraud predictions.
- **AI-Powered Explanations:** Generates explanations for fraudulent predictions using Groq API.
- **Data Processing & Cleaning:** Handles missing values, categorical encoding, and feature engineering.
- **Hyperparameter Tuning:** Uses Optuna for optimizing the Random Forest model.
- **Transaction Logging:** Stores transaction results in a CSV file for auditing.

## Tech Stack

- **Backend:** Flask
- **Machine Learning:** Scikit-learn, Random Forest, Optuna
- **Database:** CSV for storing transaction predictions
- **AI Integration:** Groq API for fraud explanations

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/shawnsaldanha79/e-commerce-fraud-detection-system.git
cd ecommerce-fraud-detection-system
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the Fraud Detection Model

Run the model training script to generate a trained fraud detection model:

```bash
python train_model.py
```

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

## Project Structure

```
├── models/
│   ├── fraud_detection_model.joblib   # Trained ML model
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

## Model Training & Evaluation

- **Data Cleaning:** Missing values handled, categorical encoding applied.
- **Feature Engineering:** Extracted features from transaction date, address match, etc.
- **ML Algorithms:** Evaluated Logistic Regression, Random Forest, Decision Tree, and XGBoost.
- **Hyperparameter Optimization:** Used Optuna to tune the best-performing model.
- **Performance Metrics:** Accuracy, Confusion Matrix, Classification Report.

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

