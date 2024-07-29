from fastapi import FastAPI
import pandas as pd
import pickle

app = FastAPI()

# Chargement du modèle
model = pickle.load(open('churn_model.pkl', 'rb'))

@app.post('/predict')
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {"prediction": int(prediction[0])}
