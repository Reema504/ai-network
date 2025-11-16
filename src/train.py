import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib

# Load data
df = pd.read_csv("data/network_logs.csv")

# Select numeric columns
features = df[["bytes", "packets", "duration"]]

# Scale the data
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Train Isolation Forest model
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)
model.fit(scaled_features)

# Save model + scaler
joblib.dump(model, "model/anomaly_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")

print("Model trained and saved successfully!")
