#15.Write a function that accepts a list and returns a new list containing only unique elements.


def unique_elements(numbers):
    result = []

    for num in numbers:
        if num not in result:
            result.append(num)

    return result

arr = [1, 2, 3, 2, 4, 1, 5]
print("Unique elements =", unique_elements(arr))

