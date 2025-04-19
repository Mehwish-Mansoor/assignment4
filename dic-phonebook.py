def main():
    # Create an empty phonebook dictionary
    phonebook = {}

    while True:
        # Display menu options
        print("\nPhonebook Menu:")
        print("1. Add a contact")
        print("2. Look up a contact")
        print("3. Delete a contact")
        print("4. Display all contacts")
        print("5. Exit")

        # Get the user's choice
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a contact
            name = input("Enter the contact's name: ")
            phone = input("Enter the contact's phone number: ")
            phonebook[name] = phone
            print(f"Contact {name} added successfully.")

        elif choice == "2":
            # Look up a contact
            name = input("Enter the name to look up: ")
            if name in phonebook:
                print(f"{name}'s phone number is {phonebook[name]}.")
            else:
                print(f"Contact {name} not found.")

        elif choice == "3":
            # Delete a contact
            name = input("Enter the name to delete: ")
            if name in phonebook:
                del phonebook[name]
                print(f"Contact {name} deleted successfully.")
            else:
                print(f"Contact {name} not found.")

        elif choice == "4":
            # Display all contacts
            if phonebook:
                print("\nPhonebook Contacts:")
                for name, phone in phonebook.items():
                    print(f"{name}: {phone}")
            else:
                print("The phonebook is empty.")

        elif choice == "5":
            # Exit the program
            print("Exiting the phonebook. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()