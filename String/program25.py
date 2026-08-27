#second most frequent character 
#find the second most frequently occurring character in a string

from collections import Counter


def second_most_frequent_character(text):
	frequencies = Counter(text)
	characters = frequencies.most_common()

	if len(characters) < 2:
		return ""

	return characters[1][0]


user_input = input("Enter a string: ")
result = second_most_frequent_character(user_input)

if result:
	print("Second most frequent character:", result)
else:
	print("There is no second most frequent character.")

