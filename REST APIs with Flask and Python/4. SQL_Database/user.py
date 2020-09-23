import sqlite3
from flask_restful import Resource, reqparse

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        path = '/Users/rodho/PycharmProjects/PyCharm-Library/REST APIs with Flask and Python/4. SQL_Database/data.db'
        connection = sqlite3.connect(path)
        cursor = connection.cursor()
        query = 'SELECT * FROM users WHERE username=?'
        # The where clause limits the selection to be only the rows where the username matches the parameter

        result = cursor.execute(query,  (username,))
        # The parameters have to be in the form of a tuple, which is what we did for the username

        row = result.fetchone()     # This will get the first row of the set, if no rows, it will be None

        if row:     # If there is a row, we create a user object with the data of the row
            user = cls(row[0], row[1], row[2])
            # or user = cls(*row) which does the same thing
            # row[0] is the first column, and so on

        else:
            user = None

        connection.close()
        return user

    # This is for ID
    @classmethod
    def find_by_id(cls, _id):
        path = '/Users/rodho/PycharmProjects/PyCharm-Library/REST APIs with Flask and Python/4. SQL_Database/data.db'
        connection = sqlite3.connect(path)
        cursor = connection.cursor()
        query = 'SELECT * FROM users WHERE id=?'
        # The where clause limits the selection to be only the rows where the username matches the parameter

        result = cursor.execute(query, (_id,))
        # The parameters have to be in the form of a tuple, which is what we did for the username

        row = result.fetchone()  # This will get the first row of the set, if no rows, it will be None

        if row:  # If there is a row, we create a user object with the data of the row
            user = cls(*row)
            # or user = cls(*row) which does the same thing
            # row[0] is the first column, and so on

        else:
            user = None

        connection.close()
        return user

# The User class must not be used for the class that lets users sign up
class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True,
                        help="This field cannot be blank.")
    parser.add_argument('password', type=str, required=True,
                        help="This field cannot be blank.")

    # For users signing up, we only need a POST request to do it
    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {'message': 'A user with that username already exists.'}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        # We have to use NULL for the auto-incrementing column which is the id
        query = "INSERT INTO users VALUES (NULL, ?, ?)"


        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {'message': 'User created successfully.'}, 201

