import re
def is_valid_email(email):
    return re.match(r'^\S+@\S+\.\S+$', email)
def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

def signup():
    print("Signup Form")
    email = input("Enter your email: ")

    if not is_valid_email(email):
        print("Invalid email format.")
        return

    password = input("Create a password: ")

    if not is_valid_password(password):
        print("Password must be at least 8 characters long, contain one uppercase letter, one number, and one special character.")
        return

    print("Signup successful!")
signup()
