import re

# Accept HTML content from the user
html = input("Enter HTML content: ")

# Regular expression pattern for URLs
pattern = r'(?:https?://|www\.)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s<"]*)?'

# Extract all URLs
urls = re.findall(pattern, html)

print("\nURLs found:")
print(urls)