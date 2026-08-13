#character count
#count the number of vowels, consonants, digits, spaces and special characters in a given string
string = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
spaces = 0
special_characters = 0
vowel_list = "aeiouAEIOU"
for char in string:
    if char in vowel_list:
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1
    else:
        special_characters += 1
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special Characters:", special_characters)