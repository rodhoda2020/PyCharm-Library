from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from item import Items, Item
from security import authenticate, identity
from user import UserRegister


app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)
jwt = JWT(app, authenticate, identity)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')

# When we send a POST request to '/register', it will be call the UserRegister
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    app.run(port=5000, debug=True)

