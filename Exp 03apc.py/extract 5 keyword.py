import re
from collections import Counter

text = input("Enter research text: ").lower()

stopwords = {"the", "is", "a", "an", "and", "of", "to", "in", "for", "are"}

words = re.findall(r"\b[a-z]+\b", text)
keywords = [w for w in words if w not in stopwords and len(w) > 2]

print("Top 5 keywords:", Counter(keywords).most_common(5))