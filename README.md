# Customer Churn Prediction ML System

## Overview

This project builds a machine learning model to predict customer churn for a telecommunications company.
The goal is to identify customers who are likely to leave the service based on their account information and usage patterns.

## Dataset

The dataset contains customer information such as:

* Gender
* Senior citizen status
* Partner and dependents
* Tenure
* Internet service type
* Monthly charges
* Total charges

These features are used to train a model that predicts whether a customer will churn.

## Machine Learning Model

The model was trained using **scikit-learn**.

Steps:

1. Data preprocessing and cleaning
2. Feature encoding
3. Model training
4. Model evaluation
5. Saving the trained model

Model performance:

Accuracy: **~78%**

## Project Structure

```
customer-churn-ml-khatantamir
│
├── app
│   └── main.py            # FastAPI application
│
├── data
│   └── churn_dataset.csv  # Dataset
│
├── models
│   ├── churn_model.pkl
│   └── scaler.pkl
│
├── src
│   └── train.py           # Model training script
│
├── requirements.txt
└── README.md
```

## Technologies Used

* Python
* pandas
* scikit-learn
* FastAPI
* joblib

## Running the Project

Install dependencies:

```
pip install -r requirements.txt
```

Run the API server:

```
uvicorn app.main:app --reload
```

Open the API documentation:

```
http://127.0.0.1:8000/docs
```

## API Endpoint

POST `/predict`

Example input:

```
[0,1,0,12,85.5,1026]
```

The API returns the predicted churn result.

## Author

Khatantamir Otgonbyamba

