# Write a python program to produce the following design:
# A 
# A B 
# A B C
#if user enters n value as 5

n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()