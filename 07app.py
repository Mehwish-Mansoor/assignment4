def print_multiple(message, repeats):
    """
    Prints the given message the specified number of times.
    """
    for _ in range(repeats):
        print(message, end=" ")

def main():
    """
    Prompts the user for a message and a number of repeats, then calls print_multiple().
    """
    message = input("Please type a message: ")
    try:
        repeats = int(input("Enter a number of times to repeat your message: "))
        print_multiple(message, repeats)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of repeats.")

if __name__ == "__main__":
    main()