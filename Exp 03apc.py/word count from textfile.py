import re
from collections import Counter

with open("data.txt", "r") as file:
    text = file.read().lower()

words = re.findall(r"\b\w+\b", text)
freq = Counter(words)

print("Total words:", len(words))
print("Word frequency:", freq)
print("Top 10 words:", freq.most_common(10))