# 🏥 Athlete Injury Risk Analytics Platform  
### Predictive Analytics and Injury Risk Management in Professional Sports Using Machine Learning

A research-driven **Data Science, AI, and Machine Learning** project focused on **early injury risk detection in athletes** using physiological, workload, recovery, and injury history data.

This platform combines **feature engineering, machine learning models, and interactive dashboards** to support evidence-based decision-making in sports science and sports medicine.

---

## 📌 Project Motivation

Sports injuries are a major concern in professional and competitive athletics, often leading to:
- Reduced athlete performance
- Long-term health complications
- Increased rehabilitation costs
- Loss of team availability

Research from global sports medicine and public health organizations highlights that **overuse and workload-related injuries are largely preventable** through proper monitoring and early intervention.

This project demonstrates how **machine learning can be used as a decision-support system** to:
- Identify high-risk athletes early
- Optimize training load
- Improve recovery strategies
- Reduce injury incidence

---

## 🎯 Key Objectives

- Build a **machine learning model** to predict injury risk probability
- Engineer **clinically meaningful features** from raw athlete data
- Visualize health and workload trends through dashboards
- Provide an **interactive injury risk prediction tool**
- Present the system as a **research-grade application**

---

## 🧠 System Overview

The platform follows a standard data science workflow:

1. **Data Collection**  
   Athlete data including demographics, training load, cardiovascular metrics, recovery indicators, and injury history.

2. **Feature Engineering**  
   Creation of advanced indicators such as:
   - Load–fatigue interaction
   - Recovery stress ratio
   - Cardiovascular strain index
   - Injury history risk score

3. **Model Training**  
   A supervised machine learning classifier (XGBoost) trained to predict injury risk probability.

4. **Visualization & Prediction**  
   Interactive dashboards and a prediction interface built using Streamlit.

---

## 🗂️ Project Structure
```bash
sports_injury_ai/
│
├── app.py # Home / landing page (project overview & dataset)
│
├── pages/
│ ├── Dashboard.py # Feature-engineered analytics dashboard
│ └── Predict_Risk.py # Individual athlete injury risk prediction
│
├── data/
│ ├── raw/
│ │ └── athlete_health_data.csv # Athlete dataset
│
├── models/
│ └── injury_risk_model.pkl # Trained ML model
│
├── train_model.py # Model training & evaluation script
│
├── requirements.txt # Project dependencies
│
├── README.md # Project documentation
│
└── .venv/ # Virtual environment (not committed)
```

---

## 📊 Dataset Description

The dataset represents **multi-dimensional athlete health data**, including:

- **Demographics**: age, height, weight, BMI  
- **Training Load**: weekly load, match minutes, sprint count, distance  
- **Cardiovascular Metrics**: resting HR, training HR, HRV, VO₂ max  
- **Recovery Indicators**: sleep duration, sleep quality, fatigue  
- **Injury History**: previous injuries, severity, recency  
- **Target Variable**: injury risk (binary)

> ⚠️ Note: The dataset used in this academic project may be synthetic or anonymized for educational purposes.

---

## 🏗️ Feature Engineering Highlights

Some of the key engineered features include:

- **Load–Fatigue Index**  
  Captures the interaction between training intensity and athlete fatigue.

- **Sleep Debt**  
  Measures recovery deficit relative to recommended sleep duration.

- **Recovery Stress Ratio**  
  Indicates imbalance between fatigue and recovery capacity.

- **Cardiovascular Strain Index**  
  Represents internal physiological load.

- **Injury History Risk Score**  
  Combines injury frequency, severity, and recency.

These features improve both **model performance** and **interpretability**.

---

## 🤖 Machine Learning Model

- **Algorithm**: XGBoost Classifier  
- **Problem Type**: Binary classification (injury risk)  
- **Evaluation Focus**:
  - Recall for injury class
  - ROC-AUC
  - Probability-based risk interpretation

The model outputs a **risk probability**, not a deterministic injury prediction.

---

## 📈 Application Features

### 🏠 Home Page
- Project overview and motivation
- WHO-aligned injury prevention context
- Dataset preview and statistics

### 📊 Dashboard
- Engineered feature visualizations
- Workload vs fatigue analysis
- Recovery and cardiovascular stress trends
- Injury risk correlations

### 🚨 Injury Risk Prediction
- Individual athlete input form
- Auto-calculated dependent features (e.g., BMI, ACWR)
- Medical-style risk interpretation (Low / Elevated / High)

---

## 🛠️ Tech Stack

- **Frontend & UI**: Streamlit  
- **Data Handling**: Pandas, NumPy  
- **Machine Learning**: Scikit-learn, XGBoost  
- **Visualization**: Streamlit charts, Matplotlib  
- **Model Persistence**: Joblib  

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/sports_injury_ai.git
cd sports_injury_ai
```
2️⃣ Create virtual environment
```
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```
3️⃣ Install dependencies
```
pip install -r requirements.txt
```
4️⃣ Run the application
```
streamlit run app.py
```
📚 Academic Use & Disclaimer
This project is intended for:

Academic learning

Research demonstration

Educational evaluation

⚠️ Disclaimer:
The system is a decision-support tool and must not replace professional medical judgment.

✨ Future Enhancements
SHAP-based explainability for predictions

Athlete comparison and longitudinal tracking

Real-time sensor data integration

Deployment on cloud platforms

Model calibration using real-world datasets

👨‍💻 Author
Jigar Veera
B.Sc. Data Science
Academic Project – Data Science, AI & Machine Learning

⭐ Acknowledgements
Sports medicine and injury prevention research literature

Open-source data science, AI engineering and ML communities

Streamlit for rapid ML application development & Streamlit Cloud Community for Deployment


---
