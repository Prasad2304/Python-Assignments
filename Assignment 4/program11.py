import re

def validate_email(email):
    pattern = r'^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}$'

    if re.match(pattern, email):
        return True
    else:
        return False


# Take email from user
email = input("Enter your email address: ")

# Validate email
if validate_email(email):
    print("Valid Email Address")
else:
    print("Invalid Email Address")