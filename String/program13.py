#Shortest Word 
#Find the shortest word in a sentence. 

sentence = input("Enter a sentence: ")
words = sentence.split()
shortest_word = min(words, key=len)
print("Shortest word:", shortest_word)
