def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))

    # Double the number and print the result until it is 100 or greater
    while curr_value < 100:
        curr_value = curr_value * 2  # Double the current value
        print(curr_value, end=" ")  # Print the doubled value on the same line

if __name__ == '__main__':
    main()