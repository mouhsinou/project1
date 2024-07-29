import streamlit as st
import requests

st.set_page_config(
    page_title="Churn Prediction",
    page_icon=":chart_with_upwards_trend:",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title("Churn Prediction :chart_with_upwards_trend:")

st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .sidebar .sidebar-content {
        background-color: #fff;
        border-right: 1px solid #ddd;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.header("User Input")

# Collecting user input
senior_citizen = st.sidebar.selectbox("Senior Citizen", [0, 1])
partner = st.sidebar.selectbox("Partner", ["Yes", "No"])
dependents = st.sidebar.selectbox("Dependents", ["Yes", "No"])
tenure = st.sidebar.number_input("Tenure (months)", min_value=0, value=0)
phone_service = st.sidebar.selectbox("Phone Service", ["Yes", "No"])
multiple_lines = st.sidebar.selectbox("Multiple Lines", ["No phone service", "No", "Yes"])
internet_service = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.sidebar.selectbox("Online Security", ["No", "Yes", "No internet service"])
online_backup = st.sidebar.selectbox("Online Backup", ["Yes", "No", "No internet service"])
device_protection = st.sidebar.selectbox("Device Protection", ["No", "Yes", "No internet service"])
tech_support = st.sidebar.selectbox("Tech Support", ["No", "Yes", "No internet service"])
streaming_tv = st.sidebar.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
streaming_movies = st.sidebar.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])
contract = st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])
payment_method = st.sidebar.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
monthly_charges = st.sidebar.number_input("Monthly Charges", min_value=0.0, value=0.0)
total_charges = st.sidebar.number_input("Total Charges", min_value=0.0, value=0.0)

# Making a prediction
input_data = {
    "SeniorCitizen": senior_citizen,
    "Partner": partner,
    "Dependents": dependents,
    "tenure": tenure,
    "PhoneService": phone_service,
    "MultipleLines": multiple_lines,
    "InternetService": internet_service,
    "OnlineSecurity": online_security,
    "OnlineBackup": online_backup,
    "DeviceProtection": device_protection,
    "TechSupport": tech_support,
    "StreamingTV": streaming_tv,
    "StreamingMovies": streaming_movies,
    "Contract": contract,
    "PaperlessBilling": paperless_billing,
    "PaymentMethod": payment_method,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges,
}

# Prédiction
if st.button("Prédire"):
    response = requests.post("https://votre-backend-fastapi.onrender.com/predict", json=input_data)
    prediction = response.json()["prediction"]
    if prediction < 0.33:
        st.success("Le client n'est pas susceptible de vous quitter.")
    elif 0.33 <= prediction < 0.67:
        st.warning("Le client a un risque moyen de vous quitter.")
    else:
        st.error("Le client est susceptible de vous quitter.")

# Sidebar
st.sidebar.write("**Mes Coordonnées :**")
st.sidebar.write("**Nom:** MAMA Moussinou")
st.sidebar.write("**Email:** mamamouhsinou@gmail.com")
st.sidebar.write("**Téléphone:** +229 95231680")
st.sidebar.write("**LinkedIn:** moussinou-mama-8b6270284")

# Ajouter une photo
st.sidebar.image("mm.png", caption='MAMA Moussinou')

# Ajouter un message sous la photo
st.write("**Made by MAMA Moussinou**")
