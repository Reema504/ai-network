import pandas as pd
import joblib

# Load model + scaler
model = joblib.load("model/anomaly_model.pkl")
scaler = joblib.load("model/scaler.pkl")

# Load new logs
df = pd.read_csv("data/new_logs.csv")

features = df[["bytes", "packets", "duration"]]
scaled = scaler.transform(features)

df["anomaly"] = model.predict(scaled)

df["anomaly"] = df["anomaly"].map({1: "Normal", -1: "Anomaly"})

print(df)
df.to_csv("data/prediction_output.csv", index=False)

print("Prediction saved!")