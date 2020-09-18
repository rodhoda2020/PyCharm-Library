import functools
user = {'username': 'Jose', 'access_level': 'guest'}

def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs): # You must add the parameter
        # The issue with adding the same parameter as the one
        # in the original function is that it becomes limited
        # to that function's parameter and no other one
        # the solution to this is to add unlimited parameters
        # by writing *args, **kwargs
        if user['access_level'] == 'admin':
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


# if the original function had parameters, the
# inner function of the decorator would have no way
# of getting that same parameter
@make_secure
def get_password(panel):
    if panel == "admin":
        return '1234'
    elif panel == 'billing':
        return 'super_secure_password'
    return '1234'

print(get_password('billing'))
