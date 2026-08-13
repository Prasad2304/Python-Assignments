#Duplicate Characters 
#Print all duplicate characters in a string. 

string = input("Enter a string: ")
duplicates = set()
for char in string:
    if string.count(char) > 1:
        duplicates.add(char)
print("Duplicate characters:", duplicates)
