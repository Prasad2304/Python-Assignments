#13.	Write a function that accepts a list of numbers and returns their average.

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

arr = [10, 20, 30, 40, 50]
print("Average =", calculate_average(arr))