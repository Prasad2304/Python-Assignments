#write a python program to print 1 2 4 8 16 32....n2

n=int(input("Enter a number:"))
for i in range(n):
    print(2**i, end=" ")
    