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
    
    # RIVE factors form
    rf1 = st.checkbox("RF1")
    rf2 = st.checkbox("RF2")
    rf3 = st.checkbox("RF3")
    rf4 = st.checkbox("RF4")
    rf5 = st.checkbox("RF5")
    rf6 = st.checkbox("RF6")
    rf7 = st.checkbox("RF7")
    rf8 = st.checkbox("RF8")
    rf9 = st.checkbox("RF9")
    calcification_score = st.number_input("Calcification Score", min_value=0)

    if st.button("Submit"):
        st.success("Form submitted successfully!")
