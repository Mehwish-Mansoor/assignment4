import random

def main():
    # Generate a random number between 0 and 99
    number_to_guess = random.randint(0, 99)
    print("I am thinking of a number between 0 and 99...")

    while True:
        # Ask the user to enter a guess
        guess = int(input("Enter a guess: "))

        # Check if the guess is correct, too high, or too low
        if guess > number_to_guess:
            print("Your guess is too high")
        elif guess < number_to_guess:
            print("Your guess is too low")
        else:
            print(f"Congrats! The number was: {number_to_guess}")
            break  # Exit the loop when the guess is correct

if __name__ == '__main__':
    main()