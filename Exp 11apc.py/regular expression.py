
# import re

# txt = "Python is easy. Python is powerful. My roll number is 51."

# print("1. re.match()")
# x = re.match("Python", txt)
# print(x.group() if x else "No match")

# print("\n2. re.search()")
# x = re.search("easy", txt)
# print(x.group() if x else "No match")

# print("\n3. re.findall()")
# x = re.findall("Python", txt)
# print(x)

# print("\n4. re.finditer()")
# x = re.finditer("Python", txt)
# for i in x:
#     print(i.group(), "at position", i.start())

# print("\n5. re.split()")
# x = re.split(" ", txt)
# print(x)

# print("\n6. re.sub()")
# x = re.sub("Python", "Java", txt)
# print(x)

# print("\n7. re.compile()")
# pattern = re.compile("[0-9]+")
# x = pattern.findall(txt)
# print(x)