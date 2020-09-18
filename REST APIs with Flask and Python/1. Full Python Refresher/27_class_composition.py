# Class composition is a counterpart of inheritance
# so you build classes that use other classes

# You're gonna be using class composition much more than inheritance

class Bookshelf:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f'Bookshelf with {self.quantity} books.'


shelf = Bookshelf(300)


class Book(Bookshelf):
    def __init__(self, name, quantity):
        super().__init__(quantity)
        self.name = name

    def __str__(self):
        return f'Book {self.name}'

book = Book('Harry Potter', 120)
print(book)

# This is inheritance
# One issue with inheritance is that the sub class methods
# should have the same or more arguments. This is an issue, however
# when the arguments in the super class is irrelevant in the
# sub class.

# This is what class composition:

class BookShelf:
    def __init__(self, *books): # This will get a number of books
        self.books = books

    def __str__(self):
        return f'BookShelf with {len(self.books)} books.'


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Book {self.name}'

book = Book('Harry Potter')
book2 = Book("Python 101")

Shelf = BookShelf(book, book2)
print(Shelf)