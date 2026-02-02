import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(
    page_title="Injury Risk Prediction",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Athlete Injury Risk Prediction System")
st.caption("Medical-grade predictive analytics for professional sports")

@st.cache_resource
def load_model():
    return joblib.load("models/injury_risk_model.pkl")

model = load_model()

st.sidebar.header("🧍 Athlete Demographics")

age = st.sidebar.number_input("Age (years)", 16, 45, 25)
height_cm = st.sidebar.number_input("Height (cm)", 150, 210, 175)
weight_kg = st.sidebar.number_input("Weight (kg)", 45, 120, 72)

# -------------------------------
# AUTO-CALCULATED BMI
# -------------------------------
height_m = height_cm / 100
bmi = round(weight_kg / (height_m ** 2), 2)

st.sidebar.text_input("BMI (auto-calculated)", value=bmi, disabled=True)

# -------------------------------
# TRAINING LOAD
# -------------------------------
st.sidebar.header("🏋️ Training Load")

acute_load = st.sidebar.number_input("Acute Load (7 days)", 100, 2000, 900)
chronic_load = st.sidebar.number_input("Chronic Load (28 days avg)", 100, 2000, 1000)

acwr = round(acute_load / chronic_load, 2)
st.sidebar.text_input("ACWR (auto)", value=acwr, disabled=True)

match_minutes_last_7_days = st.sidebar.number_input("Match Minutes (7 days)", 0, 540, 180)
sprint_count = st.sidebar.number_input("Sprint Count", 0, 400, 120)
total_distance_km = st.sidebar.number_input("Total Distance (km)", 1.0, 30.0, 10.5)

distance_per_sprint = round(total_distance_km / max(sprint_count, 1), 3)
st.sidebar.text_input("Distance per Sprint (km)", value=distance_per_sprint, disabled=True)

# -------------------------------
# CARDIOVASCULAR METRICS
# -------------------------------
st.sidebar.header("❤️ Cardiovascular")

resting_hr = st.sidebar.number_input("Resting HR", 40, 90, 58)
avg_training_hr = st.sidebar.number_input("Avg Training HR", 90, 190, 145)
hrv = st.sidebar.number_input("HRV", 10, 120, 45)
vo2_max = st.sidebar.number_input("VO₂ Max", 30, 75, 54)

cardio_strain = round(avg_training_hr / resting_hr, 2)
st.sidebar.text_input("Cardio Strain Index", value=cardio_strain, disabled=True)

# -------------------------------
# RECOVERY METRICS
# -------------------------------
st.sidebar.header("😴 Recovery")

sleep_hours = st.sidebar.number_input("Sleep Hours", 3.0, 10.0, 7.2)
sleep_quality = st.sidebar.number_input("Sleep Quality", 0, 100, 80)
fatigue = st.sidebar.number_input("Fatigue Score", 0, 100, 65)
muscle_soreness = st.sidebar.number_input("Muscle Soreness", 0, 100, 55)
perceived_exertion = st.sidebar.number_input("RPE", 1, 10, 6)

recovery_index = round((sleep_quality + hrv + sleep_hours * 10) / 3, 2)
st.sidebar.text_input("Recovery Index", value=recovery_index, disabled=True)

# -------------------------------
# INJURY HISTORY
# -------------------------------
st.sidebar.header("🩺 Injury History")

previous_injury_count = st.sidebar.number_input("Previous Injuries", 0, 10, 1)
days_since_last_injury = st.sidebar.number_input("Days Since Last Injury", 0, 2000, 120)
injury_severity_score = st.sidebar.number_input("Injury Severity Score", 0, 5, 2)

# -------------------------------
# MODEL INPUT (ORDER MUST MATCH TRAINING)
# -------------------------------
input_df = pd.DataFrame([[
    age, height_cm, weight_kg, bmi,
    acute_load, acwr, match_minutes_last_7_days,
    sprint_count, total_distance_km, resting_hr,
    avg_training_hr, hrv, vo2_max,
    sleep_hours, sleep_quality, fatigue,
    muscle_soreness, perceived_exertion,
    previous_injury_count, days_since_last_injury,
    injury_severity_score
]])

# -------------------------------
# PREDICTION
# -------------------------------
st.markdown("## 🔍 Injury Risk Prediction")

if st.button("🚨 Predict Injury Risk", use_container_width=True):
    prob = model.predict_proba(input_df)[0][1] * 100

    if prob < 30:
        st.success(f"🟢 LOW RISK — {prob:.2f}%")
    elif prob < 60:
        st.warning(f"🟡 MODERATE RISK — {prob:.2f}%")
    else:
        st.error(f"🔴 HIGH RISK — {prob:.2f}%")

    st.progress(int(prob))

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("⚕️ Research-grade Injury Risk System | Built with XGBoost + Streamlit")
