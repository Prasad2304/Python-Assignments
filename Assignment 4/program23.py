import re

file_name = input("Enter input file name: ")
target = input("Enter word/phrase to find: ")
replacement = input("Enter replacement word/phrase: ")

choice = input("Case-sensitive replacement? (yes/no): ")

with open(r"C:\Users\Prasad\Desktop\Python\Assignment 4\sample_23.txt", "r") as file:
    text = file.read()

if choice.lower() == "yes":
    count = text.count(target)
    new_text = text.replace(target, replacement)

else:
    pattern = re.escape(target)
    new_text, count = re.subn(
        pattern,
        replacement,
        text,
        flags=re.IGNORECASE
    )

output_file = "output.txt"

with open(output_file, "w") as file:
    file.write(new_text)

print("Replacement completed successfully.")
print("Number of replacements:", count)
print("Modified file saved as:", output_file)