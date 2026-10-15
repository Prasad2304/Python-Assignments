#38.	Take a list of numbers, use map() and a lambda function to generate a list containing their squares.

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda n: n * n, numbers))

print("Squares =", squares)