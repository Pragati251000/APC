import re

text = input("Enter text: ")
query = input("Enter search word: ")

if query:
    count = len(re.findall(re.escape(query), text, re.I))
    result = re.sub(re.escape(query),
                    lambda m: "**" + m.group() + "**",
                    text, flags=re.I)

    print("Occurrences:", count)
    print("Highlighted text:", result)
else:
    print("Enter a search word")