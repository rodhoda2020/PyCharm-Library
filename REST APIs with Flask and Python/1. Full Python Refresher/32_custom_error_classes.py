class TooManyPagesReadError(ValueError): # Inside the parameter is the parent class that we can inherit from
    pass


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f'<Book {self.name}, read {self.pages_read} pages out of {self.page_count}'
        )

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f'You tried to read {self.pages_read + pages} pages, but this book only has '
                f'{self.page_count} pages.'
            )
        self.pages_read += pages
        print(f'You have now read {self.pages_read} pages out of {self.page_count}.')


python101 = Book('Python 101', 50)

try:
    python101.read(35)
    python101.read(50)
except TooManyPagesReadError as e:
    print(e)


#This will print the error message without showing the traceback


# The error we face is that the book contains 50 pages, but if we send two parameters
# that, together, would add up to 85, this would still be accepted by the program

# The issue with this is that it does not leave a simple message for the user
# Instead, you can use the try and except method
