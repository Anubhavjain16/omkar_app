import streamlit as st

# Initialize session state variables
if 'page' not in st.session_state:
    st.session_state.page = 1

# Function to validate the first page
def validate_patient_details():
    if all([
        st.session_state.uhid,
        st.session_state.name,
        st.session_state.height > 0,
        st.session_state.weight > 0,
        st.session_state.age > 0,
        st.session_state.gender
    ]):
        st.session_state.page = 2
    else:
        st.warning("Please fill out all required patient details before proceeding.")

# First Page: Patient Details
if st.session_state.page == 1:
    st.title("Medical Application")
    st.subheader("Patient Details")

    st.session_state.uhid = st.text_input("UHID")
    st.session_state.name = st.text_input("Name")
    st.session_state.height = st.number_input("Height (cm)", min_value=0)
    st.session_state.weight = st.number_input("Weight (kg)", min_value=0)
    st.session_state.age = st.number_input("Age", min_value=0)
    st.session_state.gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    st.session_state.present_complaints = st.text_area("Patient Complaints (optional)")

    if st.button("Next"):
        validate_patient_details()

# Second Page: RIVE Factors
elif st.session_state.page == 2:
    st.title("Medical Application")
    st.subheader("RIVE Factors")

    rf1 = st.text_input("RF1")
    rf2 = st.text_input("RF2")
    rf3 = st.text_input("RF3")
    rf4 = st.text_input("RF4")
    rf5 = st.text_input("RF5")
    rf6 = st.text_input("RF6")
    rf7 = st.text_input("RF7")
    rf8 = st.text_input("RF8")
    rf9 = st.text_input("RF9")
    calcification_score = st.number_input("Calcification Score", min_value=0)

    if st.button("Submit"):
        st.success("Form submitted successfully!")
