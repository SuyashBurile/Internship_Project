# -*- coding: utf-8 -*-

import numpy as np
import pickle
import pandas as pd
import streamlit as st

# Load model
with open("final_obesity_model.pkl", "rb") as f:
    classifier = pickle.load(f)

# Prediction function
def predict_attack(Age, Gender, Height, Weight, BMI, PhysicalActivityLevel):
    prediction = classifier.predict([[Age, Gender, Height, Weight, BMI, PhysicalActivityLevel]])
    return int(prediction[0])

# Streamlit App
def main():
    st.set_page_config(page_title="Obesity Category Predictor", page_icon="🧬", layout="centered")

    st.markdown(
        """
        <style>
        .title-box {
            background-color: #2c3e50;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 30px;
        }
        .title-box h2 {
            color: white;
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
        }
        </style>
        <div class="title-box">
            <h2>🧬 Obesity Category Prediction System</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Enter your details:")

    # Validated inputs
    Age = st.number_input("Age", min_value=1, max_value=120, value=25)
    Gender_input = st.selectbox("Gender", ("Male", "Female"))
    Gender = 1 if Gender_input == "Male" else 0
    Height = st.number_input("Height (in meters)", min_value=1.0, max_value=2.5, value=1.7, step=0.01)
    Weight = st.number_input("Weight (in kg)", min_value=30.0, max_value=200.0, value=70.0, step=0.5)
    BMI = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.5, step=0.1)
    PhysicalActivityLevel = st.slider("Physical Activity Level", 1, 4, 2)

    if st.button("Predict Category"):
        result = predict_attack(Age, Gender, Height, Weight, BMI, PhysicalActivityLevel)
        if result == 0:
            st.success("✅ Prediction: Normal Weight (Category 0)")
        elif result == 1:
            st.success("⚠️ Prediction: Obese (Category 1)")
        elif result == 2:
            st.success("📈 Prediction: Overweight (Category 2)")
        elif result == 3:
            st.success("📉 Prediction: Underweight (Category 3)")
        else:
            st.error("❌ Unexpected category predicted!")

if __name__ == '__main__':
    main()
