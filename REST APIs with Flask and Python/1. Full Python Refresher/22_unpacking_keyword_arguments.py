def named(**kwargs):
    print(kwargs)


named(name="Bob", age=25)

# The ** collects keyword arguments and stores them into
# a dictionary.

# You can also do it the other way around


def name(name, age):
    print(name, age)



details = {'name': 'Bob', 'age': 25}

name(**details)

# You can also do both:
named(**details)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f'{arg}: {value}')


print_nicely(name="Bob", age=25)

# You can also do both for * and ** arguments


def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name="Bob", age=25)

