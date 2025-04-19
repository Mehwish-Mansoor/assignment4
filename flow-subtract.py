def subtract_seven(num):
    """
    Subtracts 7 from the given number and returns the result.
    """
    return num - 7

def main():
    # Prompt the user to enter a number
    num = int(input("Enter a number: "))
    
    # Call the subtract_seven function and store the result
    result = subtract_seven(num)
    
    # Print the result
    print(f"The result after subtracting 7 is: {result}")

if __name__ == '__main__':
    main()