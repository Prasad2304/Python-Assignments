#write a python program to print even number up to n

n=int(input("Enter a number: "))

for i in range(1, n+1):
    if 1 % 2 == 0:
        print(i)


# Method 2

n=int(input("Enter a number:"))
for i in range(2, n+1, 2):
    print