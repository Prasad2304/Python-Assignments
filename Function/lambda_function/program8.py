#40.Take two lists of numbers, use map() and lambda to create a third list containing the sum of corresponding elements.

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

sums = list(map(lambda x, y: x + y, list1, list2))

print("Sums =", sums)