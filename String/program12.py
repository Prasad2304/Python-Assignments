#Longest Word 
#Find the longest word in a given sentence. 

sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = max(words, key=len)
print("Longest word:", longest_word)

