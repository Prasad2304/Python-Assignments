#write a python program to print sum of natural number up to n

n=int(input("Enter a number: "))
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
print("Sum of natural numbers up to", n, "is", sum)
