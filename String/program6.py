#Replace Characters 
#Replace all occurrences of a given character with another character. 

string = input("Enter a string: ")

old_char = input("Enter the character to be replaced: ")
new_char = input("Enter the new character: ")

new_string = ""
for char in string:
    if char == old_char:
        new_string = new_string + new_char
    else:
        new_string = new_string + char

print("update string: ",new_string)
