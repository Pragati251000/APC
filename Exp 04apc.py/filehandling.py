f = open("sample.txt", "w")
f.write("Hello Python")
f.close()

f = open("sample.txt", "r")
print(f.read())
f.close()