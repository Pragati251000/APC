text = input("Enter paragraph: ")

stopwords = ["is", "and", "the", "a", "an", "are", "of", "to", "in"]

words = text.split()
result = []

for word in words:
    if word.lower() not in stopwords:
        result.append(word)

print("Clean text:", " ".join(result))