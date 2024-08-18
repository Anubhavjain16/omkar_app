import streamlit as st

# Configure the app layout
st.set_page_config(page_title="Medical Application", layout="wide")

# Create two columns for the pages
col1, col2 = st.columns(2)

# First page: Patient Details
with col1:
    st.subheader("Patient Details")
    
    # Patient details form
    uhid = st.text_input("UHID")
    name = st.text_input("Name")
    height = st.number_input("Height (cm)", min_value=0)
    weight = st.number_input("Weight (kg)", min_value=0)
    age = st.number_input("Age", min_value=0)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    present_complaints = st.text_area("Present Complaints")

# Second page: RIVE Factors
with col2:
    st.subheader("RIVE Factors")
    
    # RIVE factors form with input boxes
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
