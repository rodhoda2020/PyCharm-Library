def multiply(*args):
    print(args)

# This function has a set of arguments that will be collected
# into a tuple when the function is called

multiply(1, 3, 5)

# Even there are three arguments, they will be placed into a tuple

# If we wanted to multiple the arguments together

def multiply_1(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total

print(multiply_1(1, 3, 5))


# Another example

def add(x, y):
    return x + y

nums = [3, 5]
add(*nums)

# This destructuring of the parameter will send each value to
# each parameter instead of just one

def apply(*args, operator):
    if operator == '*':
        return multiply(*args) # Note: You have to have the star
                               # so that the code knows it's
                               # receiving a bunch of values
    elif operator == '+':
        return sum(args)
    else:
        return 'No valid operator provided to apply().'

# This collects all the positional arguments into a tuple and also
# have a named argument.

# This is how you call it
print(apply(1, 3, 5, 7, operator='*'))
