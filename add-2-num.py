def main():
    print("This program performs basic arithmetic operations (+, -, *, /).")
    
    # Get the first number
    num1: str = input("Enter the first number: ")
    num1: int = int(num1)
    
    # Get the second number
    num2: str = input("Enter the second number: ")
    num2: int = int(num2)
    
    # Ask the user to choose an operation
    operation: str = input("Enter the operation you want to perform (+, -, *, /): ").strip()
    
    # Perform the chosen operation
    if operation == '+':
        total: int = num1 + num2
        print(f"The result of {num1} + {num2} is {total}.")
    elif operation == '-':
        total: int = num1 - num2
        print(f"The result of {num1} - {num2} is {total}.")
    elif operation == '*':
        total: int = num1 * num2
        print(f"The result of {num1} * {num2} is {total}.")
    elif operation == '/':
        if num2 != 0:  # Check for division by zero
            total: float = num1 / num2
            print(f"The result of {num1} / {num2} is {total}.")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please enter one of +, -, *, or /.")

if __name__ == '__main__':
    main()