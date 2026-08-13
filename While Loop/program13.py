#write a python program to reverse the given number
n=int(input("Enter a number: "))
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n//=10
print("The reversed number is: ",reverse)