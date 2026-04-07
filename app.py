import streamlit as st
import numpy as np
import pickle

# Load model (optional, not used for final decision)
try:
    model = pickle.load(open("model.pkl", "rb"))
except:
    model = None

st.title("🏋️ Personal Fitness Recommendation System")

st.write("Enter your details below to get fitness advice:")

# User Inputs
age = st.number_input("Enter Age", min_value=10, max_value=100, step=1)
gender = st.selectbox("Gender", ["Male", "Female"])
height = st.number_input("Height (in cm)", min_value=100, max_value=250)
weight = st.number_input("Weight (in kg)", min_value=30, max_value=200)
goal = st.selectbox("Goal", ["Weight Gain", "Fit", "Weight Loss"])

# Convert gender
gender_val = 1 if gender == "Male" else 0

# Convert goal
if goal == "Weight Gain":
    goal_val = 0
elif goal == "Fit":
    goal_val = 1
else:
    goal_val = 2

# Predict button
if st.button("Predict"):

    # BMI Calculation
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    st.subheader(f"Your BMI: {round(bmi, 2)}")

    # Category + Recommendation
    if bmi < 18.5:
        st.success("Category: Underweight")
        st.info("Recommendation: Eat more nutritious food + strength training 💪")

    elif bmi < 25:
        st.success("Category: Normal")
        st.info("Recommendation: Maintain diet + regular exercise 🏃")

    elif bmi < 30:
        st.success("Category: Overweight")
        st.info("Recommendation: Cardio + calorie deficit diet 🔥")

    else:
        st.success("Category: Obese")
        st.info("Recommendation: Strict diet + daily exercise + consult expert 🥗")

    # Optional ML Prediction
    if model:
        input_data = np.array([[age, gender_val, height, weight, goal_val]])
        ml_result = model.predict(input_data)
        st.write(f"ML Model Prediction (encoded): {ml_result[0]}")