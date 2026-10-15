#9.	Write a function that accepts a list of numbers and returns the largest element without using the built-in max() function.

def largest(numbers):
    big = numbers[0]

    for num in numbers:
        if num > big:
            big = num

    return big

arr = [10, 25, 7, 45, 30]
print("Largest element =", largest(arr))