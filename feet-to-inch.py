# Conversion factor: 1 foot = 12 inches
FEET_TO_INCHES = 12

while True:
    try:
        # Prompt the user to enter a measurement in feet
        feet = float(input("Enter the measurement in feet (or type '0' to exit): "))
        
        # Exit condition
        if feet == 0:
            print("Exiting the program. Goodbye!")
            break

        # Convert feet to inches
        inches = feet * FEET_TO_INCHES

        # Display the result
        print(f"{feet} feet is equal to {inches} inches.\n")

    except ValueError:
        print("Invalid input. Please enter a valid number for feet.")