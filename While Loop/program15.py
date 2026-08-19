#Write a python program to print the largest of n numbers

n=int(input("Enter the number of elements: "))
largest=None
i=0
while i<n:
    num=float(input("Enter a number: "))
    if largest is None or num>largest:
        largest=num
    i+=1
print("The largest number is:", largest)