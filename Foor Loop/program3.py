#write a python program to print odd number up to n

# n=int(input("Enter a number: "))
# for i in range(1, n+1):
#     if i % 2 != 0:
#         print(i)




#method 2

n=int(input("Enter a number:"))
for i in range(1, n+1, 2):
    print(i)