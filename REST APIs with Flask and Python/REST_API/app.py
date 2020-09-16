from flask import Flask, jsonify, request, render_template

# The Flask is the class and the flask is the package.

# In order for flask to know that this application is running in a unique, specific place
# We give it __name__.
app = Flask(__name__)

# What requests it is going to understand.
# There are a few, but we will use a just one

# @app.route('/') # The / indicates the 'home' page
# def home():
#     return 'Hello, World!'

# POST - used to receive data
# GET - used to send data back only

# The user would use these verbs in the opposite manner
# GET for the user is POST for the server

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]


# @app.route('/')
# def home():
#     return render_template('index.html')

# JSON is essentially LIKE a dictionary. It is a set of key value pairs.
# very useful to send data from one application to another.

# We need to convert our Python dictionary to a text so that Javascript can read
# jsonify helps us with this conversion


# POST /store data: {name:}                        This is going to create a new store with a given name
@app.route('/store', methods=['POST']) # by default, this is a GET request, but we must change it to a POST.
                                       # We do this by adding 'methods=['POST']'. If you wanted to make it
                                       # accessible with GET and POST, "...['POST', 'GET'])"
def create_store():
    request_data = request.get_json()   # This will get our data converted into Python syntax
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>                         Get a store for a given name and return some data about it
@app.route('/store/<string:name>')   # The '<string:name>' is a bit of Flask syntax, which means
                                     # that when we create our store, it can have a parameter
                                     # Example: 'http://127.0.0.1:5000/store/some_name' some_name would be the parameter
def get_store(name):
    # iterate over stores, and find the store name with the argument
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        return jsonify({'message': 'store not found.'})


# GET /store                                       Get a list of stores
@app.route('/store')
def get_stores():
    # We also cannot send a list, but a dictionary, so we must also convert the store variable
    # into a dictionary.
    return jsonify({'stores': stores})  # This converts the store variable into JSON


# POST /store/<string:name>/item {name:, price:}   Create an item within a specific store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found.'})


# GET /store/<string:name>/item                    Get all the items within a specific store
@app.route('/store/<string:name>/item', methods=['GET'])
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found.'})


app.run(port=5000)
