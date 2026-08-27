#most frequent character in a string
#find the character highest frequency

from collections import Counter


def most_frequent_character(text):
	if not text:
		return ""

	frequencies = Counter(text)
	return max(frequencies, key=frequencies.get)


user_input = input("Enter a string: ")
print("Most frequent character:", most_frequent_character(user_input))

