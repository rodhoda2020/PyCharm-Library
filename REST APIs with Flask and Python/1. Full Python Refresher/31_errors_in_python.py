def divide(dividend, divisor):
    if divisor == 0:
        print('Divisor cannot be 0.')
        return
    return dividend / divisor

divide(15, 0)

# This does not tell the program that the parameters are wrong, only the user is notified

grades= []


# if the paramater had an issue, and the program brings out some irrelevant answer

# If the program raises errors, you can catch them and fix them

# So instead we do this:

def divide2(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be 0.') # If this error occurs, the program will give you a
                                                        # traceback. It will print the error which you wrote
                                                        # the message for. This error helps with debugging



print('Welcome to the average grade program.')

# The other error handling tool is the try and except

try:
    average = divide(sum(grades), len(grades))
    print(f'The average grade is {average}.')
except ZeroDivisionError as e:
    print('There are no grades yet in your list.')
else: # This will run if no error was raised 
    print('dfd')
finally: # This will run the code regardless of errors or not
    print('ad')


# There are different types of errors:
# You