#write a python program  to check the entered number is palindrome or not

n=int(input("Enter a number:"))
original=n
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n//=10
if original==reverse:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")