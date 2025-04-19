def print_divisors(num):
    """
    Prints all divisors of the given number.
    """
    print(f"Here are the divisors of {num}")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")

def main():
    """
    Prompts the user for a number and calls print_divisors(num).
    """
    try:
        number = int(input("Enter a number: "))
        print_divisors(number)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()