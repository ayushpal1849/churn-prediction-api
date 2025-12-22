from fastapi import FastAPI, Depends
from pydantic import BaseModel
import joblib
import numpy as np
from sqlalchemy.orm import Session
from .database import engine, SessionLocal, Base
from .models import PredictionLog
from .eda import generate_eda_report

# Initialize DB
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Customer Churn Prediction API")

# Load Model
model = joblib.load("ml_model/churn_model.pkl")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Request Schema
class CustomerData(BaseModel):
    credit_score: int
    age: int
    balance: float
    is_active: int

@app.get("/")
def home():
    return {"message": "High-Performance Churn Prediction API is Running"}

@app.post("/predict")
async def predict_churn(data: CustomerData, db: Session = Depends(get_db)):
    """
    Async endpoint to predict customer churn and log to SQL DB.
    """
    # 1. Prepare Features
    features = np.array([[data.credit_score, data.age, data.balance, data.is_active]])
    
    # 2. Prediction
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features).max()
    
    result = "Will Churn" if prediction == 1 else "Will Stay"
    
    # 3. Log to Database (Optimized SQL Storage)
    db_log = PredictionLog(
        credit_score=data.credit_score,
        age=data.age,
        balance=data.balance,
        prediction=result,
        confidence=float(probability)
    )
    db.add(db_log)
    db.commit()
    
    return {
        "prediction": result,
        "confidence_score": round(float(probability), 2),
        "db_status": "Logged successfully"
    }

@app.post("/generate-eda")
async def run_eda(data: CustomerData):
    """
    Triggers automated EDA workflow using Matplotlib.
    """
    file_path = generate_eda_report(data.dict())
    return {"message": "EDA Report Generated", "path": file_path}