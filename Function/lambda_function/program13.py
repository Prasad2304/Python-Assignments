#45.Take a list of words, use filter() and lambda to find words having more than five characters.

words = ["apple", "banana", "orange", "cat", "Python", "elephant"]

result = list(filter(lambda word: len(word) > 5, words))

print("Words with more than five characters =", result)