import streamlit as st

st.title("Customer Churn Prediction")
st.write("Enter customer data to predict churn risk")

tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.slider("Monthly Charges", 0, 200, 70)
total_charges = st.slider("Total Charges", 0, 10000, 2000)

if st.button("Predict Churn"):
    churn_score = (monthly_charges / 200) * 0.5 + ((72 - tenure) / 72) * 0.4 + (total_charges / 10000) * 0.1

    if churn_score >= 0.7:
        st.error("Customer likely to churn")
    elif churn_score >= 0.4:
        st.warning("Customer has moderate churn risk")
    else:
        st.success("Customer likely to stay")
