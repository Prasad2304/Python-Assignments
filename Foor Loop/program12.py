#Write a python program to produces following design:
#1 
#2 2
#3 3 3
#if user  enters n value as 5

n = int(input("Enter a:"))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
