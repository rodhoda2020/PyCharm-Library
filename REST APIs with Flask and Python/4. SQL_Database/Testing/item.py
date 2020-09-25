import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True,
                        help='This field cannot be left blank.')

    @jwt_required
    def get(self, name):
        item = self.find_by_name(name)

        if item:
            return item
        return {'message': 'Item not found'}, 404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}

    def post(self, name):
        if self.find_by_name(name):
            return {'message': 'An item with name {} already exist.'.format(name)}
        data = Item.parser.parse_args()
        item  = {'name': data['name'], 'price': data['price']}

        try:
            self.insert(item)
        except:
            return {'message': 'An error occurred inserting the item.'}
        return item, 201

    @classmethod
    def insert(cls, name):
        pass
