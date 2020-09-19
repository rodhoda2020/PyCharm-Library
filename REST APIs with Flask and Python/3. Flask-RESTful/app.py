from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

# JWT stands for JSON web token. It is used for the obfuscation of data
# We will be encoding data.


app = Flask(__name__)
# Flask is going to be our app, and our app is going to need roots
# We will also create an API which allows us to add the resources to it

# The encryption key, must be hidden and more secure
app.secret_key = 'jose'
api = Api(app)

# This basically allows authentication for users.
# JWT is going to create a new endpoint /auth, which is sent to the authenticate function
# We then find the correct user using the username and password. If so, it will return the user
# AT this point, the auth endpoint returns a JW token. That token can be sent to the next request
# we make.
jwt = JWT(app, authenticate, identity)

items = []

# An example explaining the previous line of code:

# Note: Every resource has to be a class


class Item(Resource):
    # This decorator now causes the function to authenticate first

    parser = reqparse.RequestParser()  # This initializes a new object to parse the request
    parser.add_argument('price',  # We are defining the argument to parse the request
                        type=float,  # We give it all the features to specify what we want
                        required=True,  # To make sure no request can come through without price
                        help="This field cannot be left blank"
                        )

    @jwt_required()
    def get(self, name):
        # This is going to take self and the name of the item

        item = next(filter(lambda x: x['name'] == name, items), None)
        # The filter function acts as a for loop and checks to see if the name matches
        # from the argument. The next function would return the first item found
        # The None means that if the next function didn't find anything, it would return None
        return {'item': item}, 200 if item else 404  # For debugging, this is the valid way that JSON accepts
    # The 404 is a status code, stating things are not OK
    # Note: The most popular status code is 200

    # Note: We no longer to write 'jsonify' since Flask-RESTful already does that for us

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            # This will check to see if there is an item that matches the item name, and if so,
            # it will not create a new one.
            return {'message': 'An item with name {} already exists.'.format(name)}, 400

        # Have the variable initiation so that any errors is filtered by the if statement above
        request_var = Item.parser.parse_args()

        item = {'name': name, 'price': request_var['price']}
        items.append(item)
        return item, 201    # The 201 is the status code to notify the item has been created


    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        # We will create a new items list, which will not contain the one item
        # with the same name as the one passed as the argument
        return {'message': '{} item deleted.'.format(name)}


    def put(self, name):
        data = Item.parser.parse_args()          # The JSON request will be send through the parser then to data

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
            # This would update with the entire payload
            # if the payload included a name, it would change the item in the list
            # We want to make sure that only some parts of the elements can pass in
            # We can use the reqparse for this.

        return item

        # This checks to see if the item exists, if it does, it will only change the price
        # If the item exists, it will simply update the item.

class Items(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>') # This will tell our api that this resource is now accessible via api.
                                              # However, there are no roots/endpoints 'app.route...'
                                              # We add the following code after Student in the parameters that
                                              # does the same thing as the app.route()
api.add_resource(Items, '/items')

# This essentially returns the name of the student in the return line.


app.run(port=5000, debug=True) # Good for debugging
