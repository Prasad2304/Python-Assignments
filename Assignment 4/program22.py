import re

def remove_stopwords(text):
   
    stopwords = {
        "is", "am", "are", "was", "were",
        "the", "a", "an", "and", "or",
        "in", "on", "at", "to", "of",
        "for", "with", "this", "that",
        "it", "as", "by", "from"
    }

    # Extract words and punctuation separately
    words = re.findall(r'\b\w+\b|[.,!?;:]', text)

    # Remove stopwords
    cleaned_words = [
        word for word in words
        if word.lower() not in stopwords
    ]

    # Join words with proper spacing
    cleaned_text = " ".join(cleaned_words)

    # Fix spacing before punctuation
    cleaned_text = re.sub(r'\s+([.,!?;:])', r'\1', cleaned_text)

    return cleaned_text


# Accept text from the user
text = input("Enter a paragraph: ")

# Remove stopwords
result = remove_stopwords(text)

# Display cleaned text
print("\nCleaned Text:")
print(result)