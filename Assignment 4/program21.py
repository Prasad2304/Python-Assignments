#	Write a program to develop a text search feature for a simple text editor. The program should:
# Text Search Feature

text = input("Enter the text: ")

query = input("Enter search word: ")

lower_text = text.lower()
lower_query = query.lower()

count = lower_text.count(lower_query)

highlighted_text = text

import re

highlighted_text = re.sub(
    re.escape(query),
    lambda match: "**" + match.group() + "**",
    text,
    flags=re.IGNORECASE
)
print("\nNumber of occurrences:", count)

print("\nHighlighted Text:")
print(highlighted_text)