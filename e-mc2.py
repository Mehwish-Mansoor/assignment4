# Define the speed of light as a constant
C = 299792458  # Speed of light in meters per second

while True:
    try:
        # Read mass input from the user
        mass = float(input("Enter kilos of mass (or type '0' to exit): "))
        
        # Exit condition
        if mass == 0:
            print("Exiting the program. Goodbye!")
            break

        # Calculate energy using E = m * c^2
        energy = mass * C**2

        # Display the results
        print("\ne = m * C^2...")
        print(f"m = {mass} kg")
        print(f"C = {C} m/s")
        print(f"{energy} joules of energy!\n")

    except ValueError:
        print("Invalid input. Please enter a valid number for mass.")