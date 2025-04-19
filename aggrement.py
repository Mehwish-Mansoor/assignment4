def main():
     while True:
        animal = input("what is your favorite  pet animal?")
    
        print(f"My favorite pet animal is {animal}! ")
    
        pet_name = input("what is  the name of your pet name?")
    
        print(f"My pet name is {pet_name}!")

        pet_colour = input("what is  the colour of your pet animal?")
    
        print(f"My pet  animal color is {pet_colour}!")
        
        pet_fact = input("what is an interesting fact about your  pet animal?")
        print(f"An interesting tact about my pet is {pet_fact}!")
        
         # Ask the user if they want to continue or exit
         
        continue_choice = input("Do you want to enter details for another pet? (yes/no): ").strip().lower()
        if continue_choice == 'yes':
            # If the user wants to continue, the loop will repeat
            
            print("Let's enter details for another pet!")
        elif continue_choice == 'no':
            # If the user wants to exit, break the loop
            
            print("Thank you for using the program. Goodbye!")
            break
        else:
            # Handle invalid input
            
            print("Invalid choice. Please enter 'yes' or 'no'.")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()