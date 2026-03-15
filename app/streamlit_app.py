import streamlit as st
import joblib
import numpy as np

st.title("Customer Churn Prediction")
st.write("Enter customer data to predict churn risk")

model = joblib.load("models/churn_model.pkl")

tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.slider("Monthly Charges", 0, 200, 70)
total_charges = st.slider("Total Charges", 0, 10000, 2000)

if st.button("Predict Churn"):

    X = np.array([[tenure, monthly_charges, total_charges]])

    pred = model.predict(X)[0]

    if pred == 1:
        st.error("Customer likely to churn")
    else:
        st.success("Customer likely to stay")
