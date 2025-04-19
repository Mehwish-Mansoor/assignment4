MAX_LENGTH = 3  # Maximum allowed length of the list

def shorten(lst):
    """Removes elements from the end of the list until its length is MAX_LENGTH."""
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove the last element
        print(f"Removed: {removed_item}")  # Print the removed element

def main():
    # Initialize an empty list
    lst = []

    while True:
        # Prompt the user to enter a value
        value = input("Enter a value (or press enter to stop): ")
        
        # Check if the user pressed enter without typing anything
        if value == "":
            break
        
        # Add the value to the list
        lst.append(value)
    
    # Print the original list
    print("Original list:", lst)
    
    # Call the shorten function to modify the list
    shorten(lst)
    
    # Print the shortened list
    print("Shortened list:", lst)

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()