def main():
    # Define the maximum value for the Fibonacci sequence
    MAX_VALUE = 10000

    # Initialize the first two terms of the Fibonacci sequence
    fib1, fib2 = 0, 1

    # Print the first term
    print(fib1, end=" ")

    # Loop to generate and print Fibonacci terms less than MAX_VALUE
    while fib2 < MAX_VALUE:
        print(fib2, end=" ")
        fib1, fib2 = fib2, fib1 + fib2  # Update to the next Fibonacci terms

if __name__ == '__main__':
    main()