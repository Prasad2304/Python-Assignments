#44.	Take a list of numbers, use filter() and lambda to find numbers greater than 50.

numbers = [10, 60, 45, 80, 30, 55, 100]

result = list(filter(lambda n: n > 50, numbers))

print("Numbers greater than 50 =", result)