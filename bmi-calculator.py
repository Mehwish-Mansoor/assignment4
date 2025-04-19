import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="BMI Calculator", page_icon="📅", layout="centered")

# Title and description
st.title("BMI Calculator")
st.markdown("""
    This is a simple BMI calculator. Enter your weight and height to calculate your BMI.
""")

# Input fields for weight and height
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Weight (kg):", min_value=0.0, max_value=300.0, value=70.0, step=0.1, format="%.2f")
with col2:
    height = st.number_input("Height (cm):", min_value=0.0, max_value=300.0, value=170.0, step=0.1, format="%.2f")

# Calculate BMI if valid inputs are provided
if height > 0 and weight > 0:
    height_m = height / 100  # Convert height to meters
    bmi = weight / (height_m ** 2)  # BMI formula

    # Display the BMI result
    st.markdown("<h3 style='text-align: center;'>Your BMI is:</h3>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center;'>{bmi:.2f}</h2>", unsafe_allow_html=True)

    # Display BMI category
    if bmi < 18.5:
        st.markdown("<h4 style='text-align: center; color: red;'>Underweight</h4>", unsafe_allow_html=True)
    elif 18.5 <= bmi < 24.9:
        st.markdown("<h4 style='text-align: center; color: green;'>Normal weight</h4>", unsafe_allow_html=True)
    elif 25 <= bmi < 29.9:
        st.markdown("<h4 style='text-align: center; color: orange;'>Overweight</h4>", unsafe_allow_html=True)
    else:
        st.markdown("<h4 style='text-align: center; color: red;'>Obesity</h4>", unsafe_allow_html=True)
else:
    st.warning("Please enter a valid weight and height.")