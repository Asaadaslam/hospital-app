import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize session state for patient data
if "patients" not in st.session_state:
    st.session_state.patients = []

# Title
st.title("🏥 Hospital Patient Management System")

# Sidebar menu
menu = st.sidebar.selectbox("Menu", ["Add Patient", "View Patients", "Generate Slip"])

# Add Patient Form
if menu == "Add Patient":
    st.header("➕ Add New Patient")
    name = st.text_input("Patient Name")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    contact = st.text_input("Contact Number")
    symptoms = st.text_area("Symptoms")

    if st.button("Add Patient"):
        patient = {
            "ID": len(st.session_state.patients) + 1,
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Contact": contact,
            "Symptoms": symptoms,
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        st.session_state.patients.append(patient)
        st.success("Patient added successfully!")

# View Patients
elif menu == "View Patients":
    st.header("📋 Patient Records")
    if st.session_state.patients:
        df = pd.DataFrame(st.session_state.patients)
        st.dataframe(df)
    else:
        st.info("No patient records found.")

# Generate Slip
elif menu == "Generate Slip":
    st.header("🧾 Patient Slip Generator")
    if st.session_state.patients:
        selected_id = st.selectbox("Select Patient ID", [p["ID"] for p in st.session_state.patients])
        selected_patient = next(p for p in st.session_state.patients if p["ID"] == selected_id)

        st.subheader("Patient Slip")
        st.text(f"Hospital Slip - {selected_patient['Date']}")
        st.text(f"ID: {selected_patient['ID']}")
        st.text(f"Name: {selected_patient['Name']}")
        st.text(f"Age: {selected_patient['Age']}")
        st.text(f"Gender: {selected_patient['Gender']}")
        st.text(f"Contact: {selected_patient['Contact']}")
        st.text(f"Symptoms: {selected_patient['Symptoms']}")
    else:
        st.info("No patients available to generate slip.")
