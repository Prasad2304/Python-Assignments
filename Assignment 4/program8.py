import string

# Accept two strings
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Function to normalize the string
def normalize(s):
    s = s.lower()
    s = s.translate(str.maketrans("", "", string.punctuation))
    s = s.replace(" ", "")
    return s

# Normalize both strings
str1 = normalize(str1)
str2 = normalize(str2)

# Create frequency dictionaries
freq1 = {}
freq2 = {}

# Count characters in first string
for ch in str1:
    if ch in freq1:
        freq1[ch] += 1
    else:
        freq1[ch] = 1

# Count characters in second string
for ch in str2:
    if ch in freq2:
        freq2[ch] += 1
    else:
        freq2[ch] = 1

# Compare frequencies
if freq1 == freq2:
    print("The strings are Anagrams.")
else:
    print("The strings are NOT Anagrams.")