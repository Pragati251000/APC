import mymodule

filename = input("Enter file name: ")

data = mymodule.read_file(filename)

print("File content:")
print(data)