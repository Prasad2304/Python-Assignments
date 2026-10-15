#3.	Define a function that accepts two numbers and returns the greater number

def greater(a, b):
    if a > b:
        return a
    else:
        return b

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print("Greater number =", greater(n1, n2))