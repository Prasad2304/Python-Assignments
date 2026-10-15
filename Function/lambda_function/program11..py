#43.	Use filter() and lambda to extract positive numbers from a list.

numbers = [-5, 10, -2, 7, 0, -8, 4]

positive = list(filter(lambda n: n > 0, numbers))

print("Positive numbers =", positive)