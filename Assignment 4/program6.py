# Vocabulary analysis of two books

book1 = set(input("Enter words of Book 1: ").lower().split())
book2 = set(input("Enter words of Book 2: ").lower().split())

# Unique words in each book
print("Unique words in Book 1:", book1)
print("Unique words in Book 2:", book2)

# Common words
common = book1.intersection(book2)
print("Common words:", common)

# Words unique to Book 1
only_book1 = book1.difference(book2)
print("Words unique to Book 1:", only_book1)

# Words unique to Book 2
only_book2 = book2.difference(book1)
print("Words unique to Book 2:", only_book2)

# Total unique words
total_unique = book1.union(book2)
print("Total unique words:", len(total_unique))