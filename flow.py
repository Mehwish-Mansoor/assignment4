ADULT_AGE = 18  # Define the age at which someone is considered an adult

def is_adult(age):
    """
    Returns True if the age is greater than or equal to ADULT_AGE, otherwise False.
    """
    return age >= ADULT_AGE

def main():
    # Prompt the user to enter an age
    age = int(input("How old is this person?: "))
    
    # Call the is_adult function and print the result
    print(is_adult(age))

if __name__ == '__main__':
    main()