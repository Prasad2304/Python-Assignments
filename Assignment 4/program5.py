text = input("Enter a paragraph: ")

# Convert text to lowercase
text = text.lower()

# Split text into words
words = text.split()

# Total number of words
print("Total number of words:", len(words))

# Count word frequency
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word Frequency:")
for word, count in frequency.items():
    print(word, ":", count)

# Top 3 most frequent words
top_3 = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:3]

print("Top 3 Most Frequent Words:")
for word, count in top_3:
    print(word, ":", count)

# Count vowels
vowels = "aeiou"
vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1

print("Total number of vowels:", vowel_count)