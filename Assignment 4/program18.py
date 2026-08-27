import re

with open(r"C:\Users\Prasad\Desktop\Python\Assignment 4\sample_18.txt", "r") as file:
    files = file.read().splitlines()

extension_count = {}

for filename in files:
    match = re.search(r'\.[a-zA-Z0-9]+$', filename)

    if match:
        extension = match.group()

        if extension in extension_count:
            extension_count[extension] += 1
        else:
            extension_count[extension] = 1

print("File Extension Count:")
print(extension_count)