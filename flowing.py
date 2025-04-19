def add_three_copies(lst, data):
    """Adds three copies of the data to the list."""
    lst.append(data)
    lst.append(data)
    lst.append(data)

def main():
    # Prompt the user for a message
    message = input("Enter a message to copy: ")

    # Create an empty list
    my_list = []

    # Display the list before modification
    print("List before:", my_list)

    # Call the helper function to add three copies of the message
    add_three_copies(my_list, message)

    # Display the list after modification
    print("List after:", my_list)

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()