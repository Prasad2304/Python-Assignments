#Email Validator
#validate whether a given email address follows a valid format

import re


def is_valid_email(email):
	pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
	return re.fullmatch(pattern, email) is not None


user_input = input("Enter an email address: ")

if is_valid_email(user_input):
	print("Valid email address")
else:
	print("Invalid email address")

