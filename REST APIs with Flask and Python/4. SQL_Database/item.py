from flask_restful import Resource, reqparse
import sqlite3
from flask_jwt import jwt_required

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True,
                        help='This field cannot be left blank.')
    @jwt_required()
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
            return {'message': 'An item with name {} already exists.'.format(name)}, 400
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}

        # We also need to deal with exceptions
        # We will put the try and except methods so we are notified if it failed.
        try:
            self.insert(item)
        except:
            return {'message': 'An error occurred inserting the item.'}, 500
            # We will return the 500 (Internal Server Error) which is stated when something goes wrong
            # but it was not the user's fault.

        return item, 201

    # We will is a class method to have the action of inserting an item into the database, centralized.
    # We will call it whenever necessary (POST, PUT, etc.)
    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        # This would delete the row that has the corresponding name
        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()
        return {'message': 'Item {} deleted.'.format(name)}

    def put(self, name):
        data = Item.parser.parse_args()

        item = self.find_by_name(name)
        updated_item = {'name': name, 'price': data['price']}
        if item is None:
            try:
                self.insert(updated_item)
            except:
                return {'message': 'An error occurred inserting the item'}, 500
        else:
            try:
                self.update(updated_item)
            except:
                return {'message': 'An error occurred updating the item'}, 500

        return updated_item

    # This is updating a row in the database
    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        # This is will update the price of the row that has the corresponding name
        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (item['price'], item['name']))

        connection.commit()
        connection.close()
class Items(Resource):

    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        # The query selects everything from the items table
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        # If we iterate the result, we can get each row
        for row in result:
            items.append({'name': row[0], 'price': row[1]})
        connection.commit()
        connection.close()

        return {'items': items}