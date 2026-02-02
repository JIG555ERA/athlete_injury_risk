import streamlit as st
import pandas as pd

st.set_page_config(page_title="Athlete Health Dashboard", layout="wide")

st.title("📊 Athlete Health Analytics Dashboard")

# -------------------------------
# Load Data
# -------------------------------
data = pd.read_csv("data/raw/athlete_health_data.csv")

# -------------------------------
# Feature Engineering
# -------------------------------
data["load_fatigue_index"] = data.weekly_training_load * data.fatigue_score

data["sleep_debt"] = (8 - data.sleep_hours_avg).clip(lower=0)

data["recovery_stress_ratio"] = data.fatigue_score / (
    data.sleep_quality_score + data.heart_rate_variability + 1
)

data["cardio_strain"] = (
    data.avg_training_heart_rate / data.resting_heart_rate
)

data["injury_history_risk"] = (
    data.previous_injury_count * data.injury_severity_score
) / (data.days_since_last_injury + 1)

# -------------------------------
# KPI Metrics
# -------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Athletes", len(data))
col2.metric("Avg Fatigue Score", round(data.fatigue_score.mean(), 1))
col3.metric("Injury Rate", f"{data.injury_risk.mean() * 100:.1f}%")
col4.metric("Avg Sleep Debt (hrs)", round(data.sleep_debt.mean(), 2))

# -------------------------------
# Visual Analytics
# -------------------------------
st.subheader("🏋️ Load vs Fatigue (Injury Highlighted)")
st.scatter_chart(
    data,
    x="weekly_training_load",
    y="fatigue_score",
    color="injury_risk"
)

st.subheader("😴 Sleep Debt vs Injury Risk")
st.scatter_chart(
    data,
    x="sleep_debt",
    y="injury_risk"
)

st.subheader("❤️ Cardiovascular Strain Distribution")
st.bar_chart(
    data["cardio_strain"]
)

st.subheader("⚠️ Recovery Stress Ratio (High = Dangerous)")
st.line_chart(
    data.sort_values("recovery_stress_ratio")["recovery_stress_ratio"]
)

st.subheader("🩺 Injury History Risk Score")
st.scatter_chart(
    data,
    x="injury_history_risk",
    y="injury_risk"
)
