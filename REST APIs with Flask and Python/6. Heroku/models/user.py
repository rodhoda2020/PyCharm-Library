import sqlite3
from db import db

# The user class is not a resource because the API cannot receive data
# into this class


# This is a model.
# A model is our internal representation of an entity.
# A resource would be the external representation of an entity.
class UserModel(db.Model):
    __tablename__ = 'users'
    # We are telling SQLAlchemy there is a column called ID
    # it is a integer, and the primary key will create an
    # index based on it
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id)