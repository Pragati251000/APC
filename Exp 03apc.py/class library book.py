class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.status = "Available"

    def borrow(self):
        self.status = "Borrowed"

    def return_book(self):
        self.status = "Available"

    def show_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)
        print("Status:", self.status)


b = Book("Python", "John", 2024)
b.show_details()
b.borrow()
b.show_details()
b.return_book()
b.show_details()