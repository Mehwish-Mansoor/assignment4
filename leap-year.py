while True:
    try:
        # Prompt the user to enter a year
        year = int(input("Enter a year (or type '0' to exit): "))
        
        # Exit condition
        if year == 0:
            print("Exiting the program. Goodbye!")
            break

        # Check if the year is a leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a leap year!\n")
        else:
            print(f"{year} is not a leap year.\n")

    except ValueError:
        print("Invalid input. Please enter a valid year.")