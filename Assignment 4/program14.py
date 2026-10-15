import re

def check_password(password):
    # Check minimum 8 characters
    if not re.search(r'.{8,}', password):
        return False

    # Check uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Check lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Check digit
    if not re.search(r'\d', password):
        return False

    # Check special character
    if not re.search(r'[!@#$%^&*()_\-]', password):
        return False

    return True


# Accept password from user
password = input("Enter your password: ")

# Check password strength
if check_password(password):
    print("Strong Password")
else:
    print("Weak Password")