from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
# Flask is going to be our app, and our app is going to need roots
# We will also create an API which allows us to add the resources to it
api = Api(app)


items = []

# An example explaining the previous line of code:

# Note: Every resource has to be a class


class Item(Resource):
    def get(self, name):
        # This is going to take self and the name of the student
        for i in items:
            if i["name"] == name:
                return i
        return {'item': None}, 404  # For debugging, this is the valid way that JSON accepts
    # The 404 is a status code, stating things are not OK
    # Note: The most popular status code is 200

    # Note: We no longer to write 'jsonify' since Flask-RESTful already does that for us

    def post(self, name):
        request_var = request.get_json(silent=True)
        # The 'silent=True' will tell the program to return None if the content-type is not set right

        item = {'name': name, 'price': request_var['price']}
        items.append(item)
        return item, 201    # The 201 is the status code to notify the item has been created

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
