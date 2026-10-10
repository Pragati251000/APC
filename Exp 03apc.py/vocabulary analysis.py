book1 = set(input("Enter first book text: ").lower().split())
book2 = set(input("Enter second book text: ").lower().split())

print("Book 1 words:", book1)
print("Book 2 words:", book2)
print("Common words:", book1 & book2)
print("Only book 1:", book1 - book2)
print("Only book 2:", book2 - book1)
print("Total unique words:", len(book1 | book2))