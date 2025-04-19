def double(num):
    """
    Returns the result of multiplying num by 2.
    """
    return num * 2

def main():
    """
    Asks the user for a number, calls double(num), and prints the result.
    """
    try:
        number = float(input("Enter a number: "))
        result = double(number)
        print(f"Double that is {result}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()