import re

text = input("Enter word or phrase: ").lower()

text = re.sub(r"[^a-z0-9]", "", text)

if text == text[::-1]:
    print(True)
else:
    print(False)