from user import User
from werkzeug.security import safe_str_cmp


def authenticate(username, password):
    # Now we change this so that it sends it to the user file to check with the database
    # user = username_mapping.get(username, None)
    user = User.find_by_username(username)

    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)