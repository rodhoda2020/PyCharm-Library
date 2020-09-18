def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be 0.')

    return dividend / divisor

def calculate(*values, operator):
    # The operator here acts as a function, even though we did not initialize it
    return operator(*values)


result = calculate(20, 4, operator=divide)
print(result)


# Another example

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f'Could not find an element with {expected}.')


friends = [
    {'name': 'Rolf Smith', 'age': 24},
    {'name': 'Adam Wool', 'age': 35},
    {'name': 'Anne Punn', 'age': 51},
]


def get_friend_name(friend):
    return friend['name']


print(search(friends, 'Rolf Smith', get_friend_name))


