#write a python program to find the sum of digits of a given number
n=int(input("Enter a Number: "))
sum=0
while n>0:
    sum+=n%10
    n//=10
    print("The sum of digits is: ",sum)
   