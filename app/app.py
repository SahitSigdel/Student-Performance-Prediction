import streamlit as st
import pandas as pd
import pickle
import os

# Loading the model which was saved as a pickle file

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "gpa_model.pkl"
)

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)
    
# Streamlit App

st.set_page_config(page_title="Student GPA Prediction", page_icon="#")

st.title("# Student GPA Prediction System")
st.write("Enter the student's information below to predict GPA.")


# User Inputs


Age = st.number_input("Age", min_value=15, max_value=20, value=17)

Gender = st.selectbox("Gender", [0, 1])

Ethnicity = st.selectbox("Ethnicity", [0, 1, 2, 3])

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
    "Number of Absences",
    min_value=0,
    max_value=50,
    value=5
)

Tutoring = st.selectbox("Tutoring", [0, 1])

ParentalSupport = st.selectbox(
    "Parental Support",
    [0, 1, 2, 3, 4]
)

Extracurricular = st.selectbox("Extracurricular Activities", [0, 1])

Sports = st.selectbox("Sports", [0, 1])

Music = st.selectbox("Music", [0, 1])

Volunteering = st.selectbox("Volunteering", [0, 1])



# Prediction

if st.button("Predict GPA"):
    try:
        input_data = pd.DataFrame({
            "Age": [Age],
            "Gender": [Gender],
            "Ethnicity": [Ethnicity],
            "ParentalEducation": [ParentalEducation],
            "StudyTimeWeekly": [StudyTimeWeekly],
            "Absences": [Absences],
            "Tutoring": [Tutoring],
            "ParentalSupport": [ParentalSupport],
            "Extracurricular": [Extracurricular],
            "Sports": [Sports],
            "Music": [Music],
            "Volunteering": [Volunteering]
        })

        prediction = model.predict(input_data)
        predicted_gpa = prediction[0]

        st.write(input_data)
        st.success("The predicted GPA is: " + str(round(predicted_gpa, 2)))

    except Exception as e:
        st.error(f"Something went wrong while predicting: {e}")