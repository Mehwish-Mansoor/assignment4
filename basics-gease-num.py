import random

# Generate a random number between 0 and 99
number_to_guess = random.randint(0, 99)

print("I am thinking of a number between 0 and 99...")

while True:
    # Ask the user to enter a guess
    user_guess = int(input("Enter a guess: "))
    
    if user_guess > number_to_guess:
        print("Your guess is too high")
    elif user_guess < number_to_guess:
        print("Your guess is too low")
    else:
        print(f"Congrats! The number was: {number_to_guess}")
        break