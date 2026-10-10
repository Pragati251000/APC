import re

text = input("Enter paragraph: ")

text = re.sub(r"\b(Dr|Mr|Mrs|Ms|Prof)\.",
              r"\1<dot>", text)

sentences = re.split(r"(?<=[.!?])\s+", text)

for sentence in sentences:
    print(sentence.replace("<dot>", "."))