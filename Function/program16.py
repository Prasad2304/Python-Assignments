#16.	Create a function to find the second-largest number in a list.

def second_largest(numbers):
    unique = []

    for num in numbers:
        if num not in unique:
            unique.append(num)

    if len(unique) < 2:
        return None

    largest = second = float('-inf')

    for num in unique:
        if num > largest:
            second = largest
            largest = num
        elif num > second:
            second = num

    return second

arr = [10, 25, 7, 45, 30]
print("Second-largest number =", second_largest(arr))