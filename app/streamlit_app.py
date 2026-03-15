import streamlit as st
import requests

st.title("Customer Churn Prediction")

st.write("Enter customer data to predict churn risk")

tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.slider("Monthly Charges", 0, 200, 70)
total_charges = st.slider("Total Charges", 0, 10000, 2000)

if st.button("Predict Churn"):

    features = [tenure, monthly_charges, total_charges]

    try:
        response = requests.post(
            "http://localhost:8000/predict",
            json=features
        )

        result = response.json()

        if result["churn_prediction"] == 1:
            st.error("Customer likely to churn")
        else:
            st.success("Customer likely to stay")

    except:
        st.warning("API not running")
