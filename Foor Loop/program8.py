# Write a python program to produce following design
                # A B C
                # A B C
                # A B C     

n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(65, 68):  # ASCII values for A, B, C
        print(chr(j), end=' ')
    print()  # Move to the next line after each row