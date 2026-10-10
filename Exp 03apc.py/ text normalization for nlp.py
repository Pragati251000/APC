import re

text = input("Enter text: ").lower()

text = text.replace("don't", "do not")
text = text.replace("can't", "cannot")
text = text.replace("won't", "will not")
text = text.replace("i'm", "i am")
text = text.replace("it's", "it is")

text = re.sub(r"\d+", "", text)
text = re.sub(r"[^a-z\s]", "", text)
text = re.sub(r"\s+", " ", text).strip()

print("Normalized text:", text)