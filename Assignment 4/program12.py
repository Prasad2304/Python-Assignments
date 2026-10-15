import re

# Accept a block of text from the user
text = input("Enter a block of text: ")

# Regular expression pattern for different phone number formats
pattern = r'(?:\(\d{3}\)\s?\d{3}[-.]?\d{4}|\d{3}[-.]\d{3}[-.]\d{4}|\d{10})'

# Extract all phone numbers
phone_numbers = re.findall(pattern, text)

# Display the result
print("\nPhone numbers found:")
print(phone_numbers)