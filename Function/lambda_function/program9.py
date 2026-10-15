#41.	Take a list of integers, use filter() and lambda to extract all even numbers.

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

result = list(map(lambda a, b: a + b, list1, list2))

print("Sum of corresponding elements =", result)