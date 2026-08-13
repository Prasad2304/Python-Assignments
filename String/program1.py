#string length
#Write a program to input a string and its length without using the len() function
string = input("Enter a string: ")
length = 0
for char in string:
    length += 1
print("The length of the string is:", length)