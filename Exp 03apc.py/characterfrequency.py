from collections import Counter

text = input("Enter a string: ")
choice = input("Ignore case? (yes/no): ")

if choice.lower() == "yes":
    text = text.lower()

freq = Counter(text)

for ch, count in freq.most_common():
    print(repr(ch), ":", count)