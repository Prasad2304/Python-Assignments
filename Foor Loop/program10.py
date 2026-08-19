# Write a python program to produce the following design:
# A B C
# A B 
# A 
#if user enters n value as 5

n = int(input("Enter n: ")) 
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end="")
        print(" ", end="")
    print()

              