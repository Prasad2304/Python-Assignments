#Reverse a string
#reverse the given string without using built-in reverse() function
string = input("Enter a string: ")
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print("Reversed string:", reversed_string)
