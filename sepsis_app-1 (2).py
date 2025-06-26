
import streamlit as st
import numpy as np

def predict_sepsis(hr, rr, sbp, dbp, temp, wbc, lactate):
    score = 0
    if hr > 110: score += 1
    if rr > 24: score += 1
    if sbp < 100: score += 1
    if temp > 38.5: score += 1
    if wbc > 12: score += 1
    if lactate > 2.2: score += 1
    return 1 if score > 3 else 0

st.title("🧪 Sepsis Risk Prediction Tool")
st.write("Input patient vitals to assess risk of early sepsis")

hr = st.number_input("Heart Rate (bpm)", value=100)
rr = st.number_input("Respiratory Rate (breaths/min)", value=22)
sbp = st.number_input("Systolic BP (mmHg)", value=110)
dbp = st.number_input("Diastolic BP (mmHg)", value=70)
temp = st.number_input("Temperature (°C)", value=38.0, step=0.1)
wbc = st.number_input("WBC Count (×10⁹/L)", value=10.0, step=0.1)
lactate = st.number_input("Serum Lactate (mmol/L)", value=1.5, step=0.1)

if st.button("Predict Sepsis Risk"):
    result = predict_sepsis(hr, rr, sbp, dbp, temp, wbc, lactate)
    if result == 1:
        st.error("⚠️ High Risk of Sepsis! Immediate action recommended.")
    else:
        st.success("✅ Low Risk of Sepsis.")

st.markdown("---")
st.caption("Tool for educational use. Not a substitute for clinical judgment.")
