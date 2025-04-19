def get_last_element(lst):
    """Prints the last element of the list."""
    print(f"The last element in the list is: {lst[-1]}")

def main():
    # Prompt the user to input the list
    n = int(input("Enter the number of elements in the list: "))
    lst = []
    for _ in range(n):
        element = input("Enter an element: ")
        lst.append(element)
    
    # Call the function to print the last element
    get_last_element(lst)

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()