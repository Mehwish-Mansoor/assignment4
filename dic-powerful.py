import hashlib  

def hash_password(password):
    """
    Hashes a password using SHA256 and returns the hexadecimal representation of the hash.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    """
    Checks if the hash of the provided password matches the stored hash for the given email.
    
    Args:
    - email: The email address of the user.
    - password_to_check: The password to verify.
    - stored_logins: A dictionary where keys are emails and values are hashed passwords.
    
    Returns:
    - True if the password matches, False otherwise.
    """
    # Hash the password to check
    hashed_password = hash_password(password_to_check)
    
    # Compare the hashed password with the stored hash for the email
    return stored_logins.get(email) == hashed_password

def main():
    # Example stored logins (email: hashed_password)
    stored_logins = {
        "user1@example.com": hash_password("mypassword123"),
        "user2@example.com": hash_password("securepassword456"),
        "user3@example.com": hash_password("anotherpassword789"),
    }

    # Test the login function
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if login(email, password, stored_logins):
        print("Login successful!")
    else:
        print("Invalid email or password.")

if __name__ == '__main__':
    main()