def greet(name):
    """
    Prints a greeting for the given name.
    """
    print(f"Greetings {name}!")

def main():
    # Prompt the user for their name
    name = input("What's your name? ")
    
    # Call the greet function
    greet(name)

if __name__ == '__main__':
    main()