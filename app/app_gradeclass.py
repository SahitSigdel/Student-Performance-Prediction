import streamlit as st
import pandas as pd
import pickle
import os

# Loading trained model
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "gradeclass_model.pkl"
)

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

# Page Title
st.title("Student Grade Class Prediction")

st.write("Enter the student's details below to predict the Grade Class.")

# User Inputs

Age = st.number_input(
    "Age",
    min_value=15,
    max_value=20,
    value=17
)

Gender = st.selectbox(
    "Gender",
    [0, 1]
)

Ethnicity = st.selectbox(
    "Ethnicity",
    [0, 1, 2, 3]
)

ParentalEducation = st.selectbox(
    "Parental Education",
    [0, 1, 2, 3, 4]
)

StudyTimeWeekly = st.number_input(
    "Study Time Weekly (Hours)",
    min_value=0.0,
    max_value=40.0,
    value=10.0
)

Absences = st.number_input(
    "Absences",
    min_value=0,
    max_value=50,
    value=5
)

Tutoring = st.selectbox(
    "Tutoring",
    [0, 1]
)

ParentalSupport = st.selectbox(
    "Parental Support",
    [0, 1, 2, 3, 4]
)

Extracurricular = st.selectbox(
    "Extracurricular Activities",
    [0, 1]
)

Sports = st.selectbox(
    "Sports",
    [0, 1]
)

Music = st.selectbox(
    "Music",
    [0, 1]
)

Volunteering = st.selectbox(
    "Volunteering",
    [0, 1]
)

# Create DataFrame

input_data = pd.DataFrame({
    "Age":[Age],
    "Gender":[Gender],
    "Ethnicity":[Ethnicity],
    "ParentalEducation":[ParentalEducation],
    "StudyTimeWeekly":[StudyTimeWeekly],
    "Absences":[Absences],
    "Tutoring":[Tutoring],
    "ParentalSupport":[ParentalSupport],
    "Extracurricular":[Extracurricular],
    "Sports":[Sports],
    "Music":[Music],
    "Volunteering":[Volunteering]
})

# Prediction

if st.button("Predict Grade Class"):

    prediction = model.predict(input_data)

    grade = prediction[0]

    st.success(f"Predicted Grade Class: {grade}")