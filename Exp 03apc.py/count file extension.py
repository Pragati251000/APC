import re

files = input("Enter filenames separated by spaces: ").split()
extensions = {}

for file in files:
    match = re.search(r"\.[A-Za-z0-9]+$", file)

    if match:
        ext = match.group().lower()
        extensions[ext] = extensions.get(ext, 0) + 1

print("Extensions:", extensions)