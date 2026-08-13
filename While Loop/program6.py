#write a python program to print even number up to n

n=int(input("Enter a number:"))
i=2
sum=0
while i<=n:
    sum+=i
    i+=2
    print("sum of even numbers up to",n, "is" , sum)
