# Character Frequency using File Handling

# Read text from file
with open(r"C:\Users\Prasad\Desktop\Python\Assignment 4\sample_10.txt", "r") as file:
    text = file.read()

# Ask user for case option
choice = input("Ignore case? (yes/no): ")

if choice.lower() == "yes":
    text = text.lower()

# Dictionary to store character frequency
frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

# Sort dictionary by frequency in descending order
sorted_frequency = sorted(
    frequency.items(),
    key=lambda x: x[1],
    reverse=True
)

# Display result
print("\nCharacter Frequency:")

for character, count in sorted_frequency:
    if character == " ":
        print("[Space] :", count)
    elif character == "\n":
        print("[New Line] :", count)
    else:
        print(character, ":", count)