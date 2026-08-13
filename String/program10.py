#ASCII Values 
#Display each character of a string along with its ASCII value.

string = input("Enter a string: ")
for char in string:
    print(f"Character: {char}, ASCII Value: {ord(char)}")
