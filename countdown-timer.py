
import streamlit as st
import time

# Add custom CSS for background and button styling
st.markdown(
    """
    <style>
    /* Background color */
    .stApp {
        background-color: #f0f8ff; /* Light blue background */
    }

    /* Button styling */
    div.stButton > button {
        background-color: #4CAF50; /* Green background */
        color: white; /* White text */
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }

    div.stButton > button:hover {
        background-color: #45a049; /* Darker green on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.title("Countdown Timer")

# Input for the countdown time in seconds
seconds = st.number_input("Enter countdown time in seconds:", min_value=0, step=1, value=10)

# Button to start the countdown
if st.button("Start Countdown"):
    st.write("Countdown started!")
    countdown_placeholder = st.empty()  # Placeholder for dynamic updates
    for i in range(seconds, -1, -1):
        mins, secs = divmod(i, 60)
        countdown_placeholder.write(f"Time left: {mins:02d}:{secs:02d}")
        time.sleep(1)
    st.write("Countdown finished!")