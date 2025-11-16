# 🔐 AI-Powered Network Log Anomaly Detector

This project is a simple **AI model** that analyzes network logs and predicts whether the traffic is **normal** or **suspicious** using a Logistic Regression classifier.

---

## 📁 Project Structure

```
ai-network/
│
├── data/
│   ├── network_logs.csv        # Training dataset
│   └── new_logs.csv            # New logs for prediction
│
├── models/
│   └── model.pkl               # Saved ML model
│
├── src/
│   ├── generate_logs.py        # Script to generate sample logs
│   ├── train.py                # Train and save the model
│   └── predict.py              # Predict anomalies from new logs
│
└── README.md                   # Project documentation
```

---

## 🚀 How It Works

### 1️⃣ Generate synthetic logs
Run:
```bash
python src/generate_logs.py
```

### 2️⃣ Train the model
```bash
python src/train.py
```

### 3️⃣ Predict anomalies from new logs
```bash
python src/predict.py
```

---

## 🧠 Model Details
- Algorithm: **Logistic Regression**
- Purpose: Detect anomalies in network traffic
- Features: `src_ip`, `dst_ip`, `protocol`, `packet_size`, `duration`

---

## 📊 Example Output
```
Source: 192.168.1.10 → Destination: 10.0.0.5
Prediction: ⚠️ Suspicious
```

---

## 🛠️ Technologies Used
- Python 3
- Pandas
- NumPy
- Scikit-learn
- Pickle
- Random data generation

---

## 👩🏻‍💻 Author
**Reema Almotiri** 
Simple AI project for learning purposes.
