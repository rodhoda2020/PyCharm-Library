from user import User
from werkzeug.security import safe_str_cmp

users = [
    User(1, 'bob', 'asdf')
]
# Our mapping also changes
username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

# userid_mapping = {1: {
#         'id': 1,
#         'username': 'bob',
#         'password': 'asdf'
# }}

# We would use the mapping variables to find users either by their name or their ID.
# This allows us not to iterate over the list everytime

# This will authenticate the user, it will select the correct username


def authenticate(username, password):
    user = username_mapping.get(username, None)
    # The .get() will give us the value of the parameter being sent
    # If there isn't a username in the mapping, it will return None
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
