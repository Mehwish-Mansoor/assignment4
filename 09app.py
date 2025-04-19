def print_ones_digit(num):
    """
    Prints the ones digit of the given integer.
    """
    ones_digit = abs(num) % 10  # Use abs() to handle negative numbers
    print(f"The ones digit is {ones_digit}")

def main():
    """
    Prompts the user for a number and calls print_ones_digit(num).
    """
    try:
        number = int(input("Enter a number: "))
        print_ones_digit(number)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()