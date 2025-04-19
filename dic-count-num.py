def main():
    # Create an empty dictionary to store the counts
    counts = {}

    while True:
        # Ask the user to enter a number
        num = input("Enter a number (or press Enter to stop): ")

        # Stop the loop if the user presses Enter without input
        if num == "":
            break

        # Convert the input to an integer
        num = int(num)

        # Update the count for the number in the dictionary
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Print the results
    for number, count in counts.items():
        print(f"{number} appears {count} times.")

if __name__ == '__main__':
    main()