from sqlalchemy import Column, Integer, Float, String, DateTime
from .database import Base
from datetime import datetime

class PredictionLog(Base):
    __tablename__ = "prediction_logs"

    id = Column(Integer, primary_key=True, index=True)
    credit_score = Column(Integer)
    age = Column(Integer)
    balance = Column(Float)
    prediction = Column(String)  # "Churn" or "Retain"
    confidence = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)