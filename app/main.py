from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# load model
model = joblib.load("models/churn_model.pkl")
scaler = joblib.load("models/scaler.pkl")

@app.get("/")
def root():
    return {"message": "Churn prediction API running"}

@app.post("/predict")
def predict(features: list[float]):
    X = np.array(features).reshape(1, -1)
    X_scaled = scaler.transform(X)
    pred = model.predict(X_scaled)[0]
    return {"churn_prediction": int(pred)}
