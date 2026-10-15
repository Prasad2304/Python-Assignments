#35.	Write a lambda function that returns True if a number is even and False otherwise.

is_even = lambda n: n % 2 == 0

num = int(input("Enter a number: "))

print(is_even(num))