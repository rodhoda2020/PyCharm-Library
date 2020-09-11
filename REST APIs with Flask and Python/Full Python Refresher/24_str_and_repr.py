class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # If you print(bob), this is what will be printed
    # It is used when you want to call your method and print a string
    def __str__(self):
        return f'Person {self.name}, {self.age} years old.'

    # The repper method is for developers to see what is being printed
    def __repr__(self):
        return f'<Person{self.name}, {self.age}'


bob = Person('Bob', 35)

# Doing this, the program will print the string of the object 'bob'
# But after creating a __str__ function, it will print what the function states

print(bob)


