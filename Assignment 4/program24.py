import re

def split_sentences(text):
    abbreviations = ["Dr.", "Mr.", "Mrs.", "Ms.", "Prof.", "St."]

    for abbr in abbreviations:
        text = text.replace(abbr, abbr.replace(".", "<DOT>"))

    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    sentences = [
        sentence.replace("<DOT>", ".").strip()
        for sentence in sentences
    ]

    return sentences

text = input("Enter a block of text: ")

sentences = split_sentences(text)

print("\nSentences:")
for sentence in sentences:
    print(sentence)