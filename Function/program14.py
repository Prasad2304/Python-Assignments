#14.Define a function that accepts a list and an element and returns the number of times that element occurs.

def count_element(numbers, element):
    count = 0

    for num in numbers:
        if num == element:
            count += 1

    return count

arr = [1, 2, 3, 2, 4, 2, 5]
element = int(input("Enter element to count: "))

print("Occurrences =", count_element(arr, element))