#write a python program to print sum of odd numbers up to n

n=int(input("Enter a number: "))
i=1
sum=0
while i<=n:
    sum+=i
    i+=2
print("Sum of odd numbers up to", n, "is", sum)