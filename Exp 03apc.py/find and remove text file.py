filename = input("Enter filename: ")
old = input("Enter word to replace: ")
new = input("Enter replacement: ")

with open(filename, "r") as file:
    text = file.read()

choice = input("Case-sensitive? (yes/no): ")

if choice.lower() == "yes":
    text = text.replace(old, new)
else:
    import re
    text = re.sub(re.escape(old), lambda m: new, text, flags=re.I)

with open("modified.txt", "w") as file:
    file.write(text)

print("Modified text saved")