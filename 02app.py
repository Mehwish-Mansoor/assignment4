def count_even():
    """
    Prompts the user to enter integers to populate a list and
    prints the number of even numbers in the list.
    """
    lst = []
    
    # Populate the list by prompting the user for integers
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            lst.append(int(user_input))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Count the number of even numbers in the list
    even_count = sum(1 for num in lst if num % 2 == 0)
    
    # Print the result
    print(f"The number of even numbers in the list is: {even_count}")

# Example usage
if __name__ == "__main__":
    count_even()