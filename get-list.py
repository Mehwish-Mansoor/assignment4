def main():
    # Initialize an empty list
    lst = []

    while True:
        # Prompt the user to enter a value
        value = input("Enter a value: ")
        
        # Check if the user pressed enter without typing anything
        if value == "":
            break
        
        # Add the value to the list
        lst.append(value)
    
    # Print the final list
    print("Here's the list:", lst)

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()