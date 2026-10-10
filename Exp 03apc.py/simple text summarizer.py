import re
from collections import Counter

text = input("Enter paragraph: ")

sentences = re.split(r"(?<=[.!?])\s+", text)
words = re.findall(r"\b\w+\b", text.lower())

stopwords = {"the", "is", "a", "an", "and", "of", "to", "in"}
freq = Counter(w for w in words if w not in stopwords)

scores = []

for sentence in sentences:
    words = re.findall(r"\b\w+\b", sentence.lower())
    score = sum(freq[w] for w in words)
    scores.append((score, sentence))

scores.sort(reverse=True)

print("Summary:")
for score, sentence in scores[:2]:
    print(sentence)