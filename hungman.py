import random

# List of words for the game
words = ["python", "hangman", "programming", "developer", "tutorial"]

# Function to play Hangman
def play_hangman():
    word = random.choice(words)  # Randomly select a word
    guessed_word = ["_"] * len(word)  # Create a placeholder for the word
    attempts = 6  # Number of attempts allowed
    guessed_letters = set()  # Keep track of guessed letters

    print("Welcome to Hangman!")
    print("Guess the word:")
    print(" ".join(guessed_word))

    while attempts > 0 and "_" in guessed_word:
        guess = input("\nEnter a letter: ").lower()

        # Check if the input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            # Reveal the guessed letter in the word
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        print(" ".join(guessed_word))

    # Check if the player won or lost
    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame over! The word was:", word)

# Start the game
if __name__ == "__main__":
    play_hangman()