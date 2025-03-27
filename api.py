from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("model.joblib")
scaler = joblib.load("scaler.joblib")

class EmployeeFeatures(BaseModel):
    features: list

@app.post("/predict")
def predict(data: EmployeeFeatures):
    scaled = scaler.transform([data.features])
    prediction = model.predict(scaled)
    return {"enrolled": int(prediction[0])}
