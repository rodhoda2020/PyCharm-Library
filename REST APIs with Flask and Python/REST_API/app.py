from flask import Flask, jsonify

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
        'name': 'My wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]


# JSON is essentially LIKE a dictionary. It is a set of key value pairs.
# very useful to send data from one application to another.

# We need to convert our Python dictionary to a text so that Javascript can read
# jsonify helps us with this conversion


# POST /store data: {name:}                        This is going to create a new store with a given name
@app.route('/store', methods=['POST']) # by default, this is a GET request, but we must change it to a POST.
                                       # We do this by adding 'methods=['POST']'. If you wanted to make it
                                       # accessible with GET and POST, "...['POST', 'GET'])"
def create_store():
    pass


# GET /store/<string:name>                         Get a store for a given name and return some data about it
@app.route('/store/<string:name>')   # The '<string:name>' is a bit of Flask syntax, which means
                                     # that when we create our store, it can have a parameter
                                     # Example: 'http://127.0.0.1:5000/store/some_name' some_name would be the parameter
def get_store(name):
    pass


# GET /store                                       Get a list of stores
@app.route('/store')
def get_stores():
    # We also cannot send a list, but a dictionary, so we must also convert the store variable
    # into a dictionary.
    return jsonify({'stores': stores})  # This converts the store variable into JSON


# POST /store/<string:name>/item {name:, price:}   Create an item within a specific store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store():
    pass


# GET /store/<string:name>/item                    Get all the items within a specific store
@app.route('/store/,<string:name>/item')
def get_items_in_store(name):
    pass


app.run(port=5000)






