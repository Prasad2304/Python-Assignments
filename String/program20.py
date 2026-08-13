#count Occurrences of a world
# a count how many times a specific world appears in a sentence

sentence = input("Enter a sentence: ")
word = input("Enter a word to count: ")
count = sentence.lower().split().count(word.lower())
print(f"The word '{word}' appears {count} times in the sentence.")
