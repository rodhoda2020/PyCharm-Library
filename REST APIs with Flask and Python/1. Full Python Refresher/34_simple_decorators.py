user = {'username': 'jose', 'access_level': 'guest'}


def get_admin_password():
    return '1234'


# We want to secure this function so that people who are guests
# cannot get the password

# This function takes in another function
def make_secure(func):
    def secure_function():
        if user['access_level'] == 'admin':
            return func()

    return secure_function

get_admin_password = make_secure(get_admin_password)
print(get_admin_password())