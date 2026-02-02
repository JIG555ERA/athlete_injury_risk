import streamlit as st
import pandas as pd

# ----------------------------------
# Page Configuration
# ----------------------------------
st.set_page_config(
    page_title="Athlete Injury Risk Analytics",
    page_icon="🏥",
    layout="wide"
)

# ----------------------------------
# HERO SECTION
# ----------------------------------
st.title("🏥 Athlete Injury Risk Analytics Platform")
st.markdown(
    """
    **A data science and machine learning–driven system for early injury risk detection in professional athletes.**  
    This platform integrates **physiological, workload, recovery, and injury history data** to support
    evidence-based decision-making in sports medicine.
    """
)

st.divider()

# ----------------------------------
# WHY THIS MATTERS (WHO-ALIGNED)
# ----------------------------------
st.subheader("🌍 Why Injury Prediction Matters in Sports")

st.markdown(
    """
    According to global sports medicine and public health research:
    
    - Sports-related injuries are a **leading cause of long-term physical impairment** in athletes.
    - Overuse injuries account for **30–50% of all sports injuries**, often caused by excessive workload and insufficient recovery.
    - Early detection and workload monitoring can **reduce injury incidence by up to 40%**.
    
    International health organizations and sports science research emphasize the role of **data-driven monitoring systems**
    to improve athlete safety, performance longevity, and rehabilitation outcomes.
    """
)

# ----------------------------------
# BENEFITS SECTION
# ----------------------------------
st.subheader("🎯 Key Benefits of This System")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        ### 🧍 Athletes
        - Reduced injury risk  
        - Optimized training loads  
        - Improved recovery awareness  
        - Longer career longevity
        """
    )

with col2:
    st.markdown(
        """
        ### 🏋️ Coaches & Trainers
        - Objective workload monitoring  
        - Early warning signals  
        - Smarter training periodization  
        - Reduced athlete downtime
        """
    )

with col3:
    st.markdown(
        """
        ### 🩺 Medical Teams
        - Injury risk stratification  
        - Evidence-based decisions  
        - Recovery tracking  
        - Preventive intervention planning
        """
    )

st.divider()

# ----------------------------------
# SYSTEM OVERVIEW
# ----------------------------------
st.subheader("🧠 How the System Works")

st.markdown(
    """
    1. **Data Collection**  
       Physiological, workload, recovery, and injury history data are collected from athletes.
    
    2. **Feature Engineering**  
       Clinically meaningful indicators such as workload ratios, fatigue interactions, and recovery stress metrics are derived.
    
    3. **Machine Learning Model**  
       An advanced ML model analyzes nonlinear patterns associated with injury occurrence.
    
    4. **Risk Prediction & Visualization**  
       Injury risk probabilities are presented through interactive dashboards and predictive tools.
    """
)

st.divider()

# ----------------------------------
# DATASET PREVIEW
# ----------------------------------
st.subheader("📊 Dataset Overview")

@st.cache_data
def load_data():
    return pd.read_csv("data/raw/athlete_health_data.csv")

data = load_data()

st.markdown(
    """
    The dataset used in this project represents **multi-dimensional athlete health data**, including:
    
    - Demographics  
    - Training load metrics  
    - Cardiovascular indicators  
    - Recovery & fatigue scores  
    - Injury history  
    """
)

st.dataframe(
    data.head(50),
    use_container_width=True
)

# ----------------------------------
# QUICK STATS
# ----------------------------------
st.subheader("📈 Dataset Summary Statistics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Records", len(data))
col2.metric("Avg Weekly Load", round(data.weekly_training_load.mean(), 1))
col3.metric("Avg Fatigue Score", round(data.fatigue_score.mean(), 1))
col4.metric("Injury Rate", f"{data.injury_risk.mean() * 100:.2f}%")

st.divider()

# ----------------------------------
# NAVIGATION HELP
# ----------------------------------
st.subheader("🧭 Explore the Platform")

st.markdown(
    """
    Use the sidebar to navigate through the system:
    
    - **Dashboard** → Visual analytics and engineered features  
    - **Predict Risk** → Individual athlete injury risk prediction  
    - **Research Insights** → Model interpretation and findings  
    """
)

# ----------------------------------
# FOOTER
# ----------------------------------
st.markdown("---")
st.caption(
    "📚 Academic Project | Data Science • Machine Learning • Sports Analytics | Built with Streamlit"
)
