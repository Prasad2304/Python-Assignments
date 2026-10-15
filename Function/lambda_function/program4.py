#36.	Use a lambda function to find the maximum of two numbers.

maximum = lambda a, b: a if a > b else b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Maximum =", maximum(x, y))