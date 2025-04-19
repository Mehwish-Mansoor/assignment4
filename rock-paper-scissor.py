import streamlit as st
import random
# Apply custom CSS 
def apply_custom_css():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #fadee0;
        }
        .stButton>button {
            background-color: #8B0A1A;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
        }
        .stButton>button:hover {
            background-color: #660066;
            color: white;
        }
        
        </style>
        """,
        unsafe_allow_html=True
    )

apply_custom_css()
# Title 
st.title("Rock🪨-Paper📃Scissors✂️ Game")

# Instructions
st.write("Choose Rock, Paper, or Scissors and play against the computer!")

# User choice
user_choice = st.selectbox("Your Choice:", ["Rock", "Paper", "Scissors"])

# Play button
if st.button("Play"):
    # Computer choice
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    st.write(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        st.write("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        st.write("You win!")
    else:
        st.write("You lose!")