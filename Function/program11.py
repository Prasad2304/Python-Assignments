#11.Write a function that accepts a string and returns its reverse.

def reverse_string(text):
    return text[::-1]

string = input("Enter a string: ")
print("Reversed string =", reverse_string(string))