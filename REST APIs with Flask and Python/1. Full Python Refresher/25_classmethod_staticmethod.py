class ClassTest:

    # All functions that use the object as the first parameter are called instance methods
    # instance methods get an object
    def instance_method(self):
        print(f'Called instance_method of {self}')

    # Class Method
    @classmethod
    # This parameter will be the class method
    # class methods get a class
    # They are used for factories
    def class_method(cls):
        print(f'Called class_method of {cls}')

    @staticmethod
    # static methods do not get anything
    # Static methods are used for putting a method into the class
    def static_method():
        print('Called static_method.')

test = ClassTest()

# Two ways of calling the instance method
test.instance_method()
ClassTest.instance_method(test)

# Class method
ClassTest.class_method()

# Static method
ClassTest.static_method()



class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr(self):
        return f'<Book {self.name}, {self.book_type}, weighing {self.weight}g>'

    @classmethod
    def hardcover(cls, name, weight):
        return cls(name, Book.Types[0], weight + 100)

    @classmethod
    def paperback(cls, name, weight):
        return cls(name, Book.TYPES[1], weight)

    # These class methods create a new object for the instance methods of the class
    # to use.

book = Book('Harry Potter', 'hardcover', 1500)

# The class methods comes into play. Say I only wanted to pass in books as hardcover or paperback.

# So, it can create a method that will take the name and weight, and a new book object of type
# 'hardcover'

book = Book.hardcover('Harry Potter', 1500)
light = Book.paperback('Python 101', 600)

print(book.name)