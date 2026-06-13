import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("placement_model.pkl", "rb"))

st.title("Student Placement Predictor")

cgpa = st.number_input("CGPA")
internships = st.number_input("Internships")
projects = st.number_input("Projects")
workshops = st.number_input("Workshops")
aptitude = st.number_input("Aptitude Score")
softskills = st.number_input("Soft Skills Rating")
extra = st.number_input("Extracurricular Activities (1=Yes,0=No)")
training = st.number_input("Placement Training (1=Yes,0=No)")
ssc = st.number_input("SSC Marks")
hsc = st.number_input("HSC Marks")

if st.button("Predict"):

    student = pd.DataFrame({
        "CGPA":[cgpa],
        "Internships":[internships],
        "Projects":[projects],
        "Workshops/Certifications":[workshops],
        "AptitudeTestScore":[aptitude],
        "SoftSkillsRating":[softskills],
        "ExtracurricularActivities":[extra],
        "PlacementTraining":[training],
        "SSC_Marks":[ssc],
        "HSC_Marks":[hsc]
    })

    result = model.predict(student)

    if result[0] == 1:
        st.success("🎉 Placed")
    else:
        st.error("❌ Not Placed")