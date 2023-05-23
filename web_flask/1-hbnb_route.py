#!/usr/bin/python3
""" This script starts a Flask web application:
    web application is listening on 0.0.0.0, port 5000
    Routes: /: display “Hello HBNB!”
    Routes: /hbnb displays HBNB
    using the option strict_slashes=False in our route definition """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def print_hello():
    """ hello_hbnb method """
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def print_hbnb():
    """This method prints HBNB"""
    return ("HBNB")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
