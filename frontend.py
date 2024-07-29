import streamlit as st
import pandas as pd
import pickle

# Chargement du modèle
model = pickle.load(open('churn_model.pkl', 'rb'))

st.set_page_config(page_title="Prédiction du Churn Client", page_icon=":bar_chart:", layout="wide")

st.title("Prédiction du Comportement d'un Client")

# Saisie des informations client
st.header("Informations Client")
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Genre", ["Male", "Female"])
    SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
    Partner = st.selectbox("Partner", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.slider("Tenure (mois)", 0, 72, 1)
    PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
    MultipleLines = st.selectbox("Multiple Lines", ["No phone service", "No", "Yes"])
    InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    OnlineSecurity = st.selectbox("Online Security", ["No internet service", "No", "Yes"])
    OnlineBackup = st.selectbox("Online Backup", ["No internet service", "No", "Yes"])

with col2:
    DeviceProtection = st.selectbox("Device Protection", ["No internet service", "No", "Yes"])
    TechSupport = st.selectbox("Tech Support", ["No internet service", "No", "Yes"])
    StreamingTV = st.selectbox("Streaming TV", ["No internet service", "No", "Yes"])
    StreamingMovies = st.selectbox("Streaming Movies", ["No internet service", "No", "Yes"])
    Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
    PaymentMethod = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
    MonthlyCharges = st.number_input("Monthly Charges")
    TotalCharges = st.number_input("Total Charges")

# Création d'un dataframe à partir des saisies
input_data = pd.DataFrame({
    'gender': [gender],
    'SeniorCitizen': [SeniorCitizen],
    'Partner': [Partner],
    'Dependents': [Dependents],
    'tenure': [tenure],
    'PhoneService': [PhoneService],
    'MultipleLines': [MultipleLines],
    'InternetService': [InternetService],
    'OnlineSecurity': [OnlineSecurity],
    'OnlineBackup': [OnlineBackup],
    'DeviceProtection': [DeviceProtection],
    'TechSupport': [TechSupport],
    'StreamingTV': [StreamingTV],
    'StreamingMovies': [StreamingMovies],
    'Contract': [Contract],
    'PaperlessBilling': [PaperlessBilling],
    'PaymentMethod': [PaymentMethod],
    'MonthlyCharges': [MonthlyCharges],
    'TotalCharges': [TotalCharges]
})

# Prédiction
if st.button("Prédire"):
    prediction = model.predict(input_data)[0]
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
