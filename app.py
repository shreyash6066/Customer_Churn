<<<<<<< HEAD
import streamlit as st
import pandas as pd
import pickle

# Load trained model and column structure
model = pickle.load(open('rf_model.pkl', 'rb'))
# list of columns used in training
model_columns = pickle.load(open('model_columns.pkl', 'rb'))

st.set_page_config(page_title="Telco Churn Prediction", layout="centered")
st.title("📞 Telco Customer Churn Prediction")

st.markdown("### Enter Customer Details")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
senior_citizen = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72, 12)
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
multiple_lines = st.selectbox(
    "Multiple Lines", ["Yes", "No", "No phone service"])
internet_service = st.selectbox(
    "Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.selectbox(
    "Online Security", ["Yes", "No", "No internet service"])
online_backup = st.selectbox(
    "Online Backup", ["Yes", "No", "No internet service"])
device_protection = st.selectbox(
    "Device Protection", ["Yes", "No", "No internet service"])
tech_support = st.selectbox(
    "Tech Support", ["Yes", "No", "No internet service"])
streaming_tv = st.selectbox(
    "Streaming TV", ["Yes", "No", "No internet service"])
streaming_movies = st.selectbox(
    "Streaming Movies", ["Yes", "No", "No internet service"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
payment_method = st.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
total_charges = round(monthly_charges * tenure, 2)

st.write(f"✅ **Auto-calculated Total Charges**: ₹ {total_charges}")

# Predict button
if st.button("Predict Churn Probability"):
    # Create input DataFrame
    user_input = {
        'gender': gender,
        'SeniorCitizen': senior_citizen,
        'Partner': partner,
        'Dependents': dependents,
        'tenure': tenure,
        'PhoneService': phone_service,
        'MultipleLines': multiple_lines,
        'InternetService': internet_service,
        'OnlineSecurity': online_security,
        'OnlineBackup': online_backup,
        'DeviceProtection': device_protection,
        'TechSupport': tech_support,
        'StreamingTV': streaming_tv,
        'StreamingMovies': streaming_movies,
        'Contract': contract,
        'PaperlessBilling': paperless_billing,
        'PaymentMethod': payment_method,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges
    }

    input_df = pd.DataFrame([user_input])

    # One-hot encoding and align with model columns
    input_encoded = pd.get_dummies(input_df)
    input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

    # Prediction
    churn_prob = model.predict_proba(input_encoded)[0][1]
    st.subheader("📊 Prediction Result")
    st.success(f"Churn Probability: {churn_prob * 100:.2f}%")
    st.info(f"No Churn Probability: {(1 - churn_prob) * 100:.2f}%")
=======
import streamlit as st
import pandas as pd
import pickle

# Load trained model and column structure
model = pickle.load(open('rf_model.pkl', 'rb'))
# list of columns used in training
model_columns = pickle.load(open('model_columns.pkl', 'rb'))

st.set_page_config(page_title="Telco Churn Prediction", layout="centered")
st.title("📞 Telco Customer Churn Prediction")

st.markdown("### Enter Customer Details")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
senior_citizen = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72, 12)
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
multiple_lines = st.selectbox(
    "Multiple Lines", ["Yes", "No", "No phone service"])
internet_service = st.selectbox(
    "Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.selectbox(
    "Online Security", ["Yes", "No", "No internet service"])
online_backup = st.selectbox(
    "Online Backup", ["Yes", "No", "No internet service"])
device_protection = st.selectbox(
    "Device Protection", ["Yes", "No", "No internet service"])
tech_support = st.selectbox(
    "Tech Support", ["Yes", "No", "No internet service"])
streaming_tv = st.selectbox(
    "Streaming TV", ["Yes", "No", "No internet service"])
streaming_movies = st.selectbox(
    "Streaming Movies", ["Yes", "No", "No internet service"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
payment_method = st.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
total_charges = round(monthly_charges * tenure, 2)

st.write(f"✅ **Auto-calculated Total Charges**: ₹ {total_charges}")

# Predict button
if st.button("Predict Churn Probability"):
    # Create input DataFrame
    user_input = {
        'gender': gender,
        'SeniorCitizen': senior_citizen,
        'Partner': partner,
        'Dependents': dependents,
        'tenure': tenure,
        'PhoneService': phone_service,
        'MultipleLines': multiple_lines,
        'InternetService': internet_service,
        'OnlineSecurity': online_security,
        'OnlineBackup': online_backup,
        'DeviceProtection': device_protection,
        'TechSupport': tech_support,
        'StreamingTV': streaming_tv,
        'StreamingMovies': streaming_movies,
        'Contract': contract,
        'PaperlessBilling': paperless_billing,
        'PaymentMethod': payment_method,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges
    }

    input_df = pd.DataFrame([user_input])

    # One-hot encoding and align with model columns
    input_encoded = pd.get_dummies(input_df)
    input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

    # Prediction
    churn_prob = model.predict_proba(input_encoded)[0][1]
    st.subheader("📊 Prediction Result")
    st.success(f"Churn Probability: {churn_prob * 100:.2f}%")
    st.info(f"No Churn Probability: {(1 - churn_prob) * 100:.2f}%")
>>>>>>> 700709f0f440b597563141d3a3733c3537e52512
