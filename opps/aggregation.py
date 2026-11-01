# Aggregation = Represents a relationship where one object (the whole)
#               contains refereces to one or more INDEPENDENT objects (the partS)

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def book_list(self):
        return [f"{book.title} by {book.author}" for book in self.books]    

class Book:
    def __init__(self, title, author):
        self.title =  title
        self.author = author

library = Library("New York Public Library")

book1 = Book("Harry Potter", "G.K Rowling")
book2 = Book("The Power Of Now", "J.L Cherry")
book3 = Book("Good Habbits", "L.R Rao")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)
for book in library.book_list():
    print(book)


