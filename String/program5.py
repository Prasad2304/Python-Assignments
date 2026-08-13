#Uppercase and Lowercase Count 
#Count the number of uppercase and lowercase letters in a string

string = input("Enter a string: ")

uppercase_count = 0
lowercase_count = 0

for char in string:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1

print("number of uppercase letters:",uppercase_count)
print("number of uppercase letters:",lowercase_count)
