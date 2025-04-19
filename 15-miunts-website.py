
    
import streamlit as st
import pandas as pd
import random

# Set page configuration (must be at the top)
st.set_page_config(page_title="Random Name Generator", page_icon=":sparkles:", layout="wide")

# Inject custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
        font-family: Arial, sans-serif;
    }
    h1 {
        color: #4CAF50;
        text-align: center;
    }
    .stDataFrame {
        border: 2px solid #4CAF50;
        border-radius: 5px;
        padding: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.title("Student CSV File Generator")

# List of names to randomly choose from
name = ["Ali", "Mehwish", "Sara", "Aliyan", "Fatima", "Ayesha", "Umm-e-Hani", "Mansoor"]

# Generate random student data
students = []
for i in range(1, 8):
    student = {
        "Name": random.choice(name),
        "Roll_No": random.randint(1, 7),
        "Age": random.randint(18, 25),
        "Grade": random.choice(["A", "B", "C"]),
        "Marks": random.randint(40, 100)
    }
    students.append(student)

# Create a DataFrame from the student data
df = pd.DataFrame(students)

# Display the generated data
st.subheader("Generated Student Data")
st.dataframe(df)

# Convert the DataFrame to CSV and provide a download button
csv_file = df.to_csv(index=False).encode('utf-8')
st.download_button(label="Download CSV", data=csv_file, file_name="student.csv", mime="text/csv")

# Success message
st.success("Student record generated successfully")