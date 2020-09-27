import sqlite3

# The user class is not a resource because the API cannot receive data
# into this class

# This is a model.
# A model is our internal representation of an entity.
# A resource would be the external representation of an entity.
class UserModel:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM users WHERE username=?'

        result = cursor.execute(query,  (username,))

        row = result.fetchone()

        if row:
            user = cls(row[0], row[1], row[2])

        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM users WHERE id=?'

        result = cursor.execute(query, (_id,))

        row = result.fetchone()
        if row:
            user = cls(*row)

        else:
            user = None

        connection.close()
        return user