#write a python program to print fibonacci series up to n

n=int(input("Enter a number: "))
a=0
b=1
print(a, b, end=" ")
i=2
while i<n:
    c=a+b
    print(c, end=" ")
    a=b
    b=c
    i+=1
    