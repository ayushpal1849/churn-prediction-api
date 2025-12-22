import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_eda_report(data: dict):
    """
    Generates a simple visualization of input data distribution.
    """
    # Convert single input to DataFrame for visualization context
    df = pd.DataFrame([data])
    
    # Create directory for images
    os.makedirs("static", exist_ok=True)
    
    # Plotting logic (Simulated EDA)
    plt.figure(figsize=(6, 4))
    categories = list(data.keys())
    values = list(data.values())
    
    plt.bar(categories, values, color=['blue', 'green', 'orange', 'red'])
    plt.title("Input Feature Distribution")
    plt.ylabel("Value")
    
    file_path = "static/eda_report.png"
    plt.savefig(file_path)
    plt.close()
    
    return file_path