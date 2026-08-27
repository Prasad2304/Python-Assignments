#word frequency dictionary
#count the frequency of every word in a paragraph

import re


def word_frequency(paragraph):
	words = re.findall(r"[A-Za-z0-9']+", paragraph.lower())
	frequency = {}

	for word in words:
		frequency[word] = frequency.get(word, 0) + 1

	return frequency


user_input = input("Enter a paragraph: ")
print("Word frequency:", word_frequency(user_input))

