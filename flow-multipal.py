def get_user_data():
    """
    Asks the user for their first name, last name, and email address,
    and returns all three as a tuple.
    """
    # Prompt the user for their first name
    first_name = input("What is your first name?: ")
    
    # Prompt the user for their last name
    last_name = input("What is your last name?: ")
    
    # Prompt the user for their email address
    email = input("What is your email address?: ")
    
    # Return the collected data as a tuple
    return first_name, last_name, email

def main():
    # Call the get_user_data function and store the returned tuple
    user_data = get_user_data()
    
    # Print the received user data
    print("Received the following user data:", user_data)

if __name__ == '__main__':
    main()