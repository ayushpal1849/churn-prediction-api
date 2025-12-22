import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# 1. Create Dummy Data (Simulating Customer Data)
data = {
    'credit_score': [600, 750, 800, 500, 650, 700, 820, 550],
    'age': [25, 45, 35, 50, 30, 40, 28, 60],
    'balance': [5000, 80000, 60000, 1000, 25000, 40000, 90000, 500],
    'is_active': [1, 1, 0, 1, 0, 1, 1, 0],  # 1=Active, 0=Inactive
    'churn': [0, 0, 1, 1, 0, 0, 0, 1]       # Target: 1=Left, 0=Stayed
}
df = pd.DataFrame(data)

# 2. Split Data
X = df.drop('churn', axis=1)
y = df['churn']

# 3. Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# 4. Save Model
os.makedirs("ml_model", exist_ok=True)
joblib.dump(model, "ml_model/churn_model.pkl")
print("✅ Model trained and saved to ml_model/churn_model.pkl")