from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
api = Api(app)

items = []

jwt = JWT(app, authenticate, identity)

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='This field cannot be left blank')

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': 'The item {} is already in items'.format(name)}
        request_var = Item.parser.parse_args()
        item = {'name': name,
                'price': request_var['price']}
        items.append(item)
        return item

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))

        return {'message': '{} item deleted.'.format(name)}

    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item:
            item.update(data)
        else:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        return item


class Items(Resource):

    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')

app.run(port=5000, debug=True)