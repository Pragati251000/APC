from collections import Counter

text = input("Enter paragraph: ").lower()
words = text.split()

print("Total words:", len(words))
print("Word frequency:", Counter(words))
print("Top 3 words:", Counter(words).most_common(3))

vowels = 0
for ch in text:
    if ch in "aeiou":
        vowels += 1

print("Vowels:", vowels)