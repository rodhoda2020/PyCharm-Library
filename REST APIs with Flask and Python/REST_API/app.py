from flask import Flask

# The Flask is the class and the flask is the package.

# In order for flask to know that this application is running in a unique, specific place
# We give it __name__.
app = Flask(__name__)

# What requests it is going to understand.
# There are a few, but we will use a just one

# This is a decorator
# Note: a decorator is a callable object that takes a function as its input parameter
# @app.route()

