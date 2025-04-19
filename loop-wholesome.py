def main():
    # Define the affirmation
    affirmation = "I am capable of doing anything I put my mind to."

    while True:
        # Prompt the user to type the affirmation
        user_input = input("Please type the following affirmation: I am capable of doing anything I put my mind to.\n")

        # Check if the user typed the affirmation correctly
        if user_input == affirmation:
            print("That's right! :)")
            break  # Exit the loop when the affirmation is typed correctly
        else:
            print("Hmmm That was not the affirmation.")

if __name__ == '__main__':
    main()