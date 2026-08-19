#write a python program to print smallest of n numbers

n = int(input("Enter the number of elements: "))
smallest = None
i = 0
while i < n:
    num = float(input("Enter a number: "))
    if smallest is None or num < smallest:
        smallest = num
    i += 1
print("The smallest number is:", smallest)