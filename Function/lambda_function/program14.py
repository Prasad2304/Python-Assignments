#46.Take a list of words; sort them according to their length using lambda.

words = ["apple", "banana", "orange", "cat", "Python", "elephant"]

sorted_words = sorted(words, key=lambda word: len(word))

print("Words sorted by length =", sorted_words)