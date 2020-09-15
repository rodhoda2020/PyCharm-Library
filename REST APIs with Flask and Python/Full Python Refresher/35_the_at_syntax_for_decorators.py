import functools
user = {'username': 'Jose', 'access_level': 'guest'}

def make_secure(func): # This is the decorator
    @functools.wraps(func)
    # You want to place this for the inner function
    # The inner function is what replaces the
    # original function
    def secure_function():
        if user['access_level'] == 'admin':
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function

@make_secure  # This works but we must add the another
              # decorator for secure_function
def get_admin_password():
    return '1234'

# one problem with this is that, if the print line
# was before the get_admin line, the decorator wouldn't
# work.

print(get_admin_password())

# The solution is the @make_secure (the function) be placed
# on top of the function
# and this would allow to to remove the
# 'get_admin_password = make_secure(get_admin_password)' line.