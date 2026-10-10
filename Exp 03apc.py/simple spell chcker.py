import re

dictionary = {"hello", "world", "python", "program", "student",
              "computer", "book", "good", "morning", "this",
              "is", "a", "simple", "language", "text"}

text = input("Enter text: ").lower()
words = re.findall(r"[a-z]+", text)

misspelled = []

for word in words:
    if word not in dictionary and word not in misspelled:
        misspelled.append(word)

print("Misspelled words:", misspelled)