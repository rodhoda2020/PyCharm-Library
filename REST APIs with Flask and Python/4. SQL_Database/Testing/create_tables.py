from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import jwt_required, JWT

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, )

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=str, required=True,
                        help='This cannot be left blank.')

    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    