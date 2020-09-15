from flask import Flask

# The Flask is the class and the flask is the package.

# In order for flask to know that this application is running in a unique, specific place
# We give it __name__.
app = Flask(__name__)

# What requests it is going to understand.
# There are a few, but we will use a just one

@app.route('/') # The / indicates the 'home' page
def home():
    return 'Hello, World!'

app.run(port=5000)
