import re

# Accept HTML content from the user
html = input("Enter HTML content: ")

# Regular expression to match HTML tags
pattern = r'<[^>]*>'

# Remove all HTML tags
cleaned_text = re.sub(pattern, '', html)

# Display cleaned text
print("\nCleaned Text:")
print(cleaned_text)