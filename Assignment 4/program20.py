#20.	Write a program to create a word count utility for analyzing a large text document. The program should:

import string

with open(r"C:\Users\Prasad\Desktop\Python\Assignment 4\sample_20.txt", "r") as file:
    text = file.read()

text = text.lower()

text = text.translate(str.maketrans("", "", string.punctuation))

words = text.split()

total_words = len(words)

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

sorted_words = sorted(
    frequency.items(),
    key=lambda x: x[1],
    reverse=True
)

print("Total number of words:", total_words)

print("\n10 Most Frequent Words:")
for word, count in sorted_words[:10]:
    print(word, ":", count)
