Customer Churn Prediction ML System
Overview

This project builds a machine learning model to predict customer churn for a telecommunications company.
Customer churn prediction helps businesses identify customers who are likely to cancel their service so that proactive retention strategies can be applied.

The system includes:

A machine learning model trained with scikit-learn

Data preprocessing and feature engineering

A FastAPI REST API for real-time predictions

A reproducible training pipeline

Dataset

The dataset contains customer account information commonly used for churn prediction.

Key features include:

Gender

Senior citizen status

Partner and dependents

Tenure

Internet service type

Monthly charges

Total charges

These variables are used as input features to train the churn prediction model.

Machine Learning Model

The model was developed using scikit-learn and trained on historical customer data.

Training pipeline steps:

Data cleaning and preprocessing

Feature encoding

Train/test data split

Model training

Model evaluation

Saving the trained model

The trained model and scaler are stored using joblib for reuse during API inference.

Model Performance

The model was evaluated using a train/test split.

Evaluation metric:

Accuracy: ~78%

This means the model correctly predicts customer churn approximately 78% of the time on unseen data.

The trained model is deployed through the FastAPI service to provide predictions via an API endpoint.

Project Structure
customer-churn-ml-khatantamir
│
├── app
│   └── main.py            # FastAPI application
│
├── data
│   └── churn_dataset.csv  # Dataset used for training
│
├── models
│   ├── churn_model.pkl    # Trained ML model
│   └── scaler.pkl         # Feature scaler
│
├── src
│   └── train.py           # Model training pipeline
│
├── requirements.txt
└── README.md
Technologies Used

Python

pandas

scikit-learn

FastAPI

joblib

Running the Project

Install dependencies:

pip install -r requirements.txt

Run the FastAPI server:

uvicorn app.main:app --reload

Open the API documentation in your browser:

http://127.0.0.1:8000/docs
API Endpoint
POST /predict

Example input:

[0,1,0,12,85.5,1026]

The API returns a prediction indicating whether the customer is likely to churn.

API Demo

Below is the FastAPI interactive documentation used to test the churn prediction model.

Author

Khatantamir Otgonbyamba
