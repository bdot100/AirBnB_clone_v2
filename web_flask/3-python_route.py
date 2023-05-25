#!/usr/bin/python3
""" This script starts a Flask web application:
    web application is listening on 0.0.0.0, port 5000
    Routes: /: display “Hello HBNB!”
    Routes: /hbnb displays "HBNB"
    Routes: /c/<text>, display “C ” followed by the value
    of the text variable (replace underscore _ symbols with
    a space )
    Routes: /python/(<text>): display “Python ”, followed
            by the value of the text variable
            (replace underscore _ symbols with a space )
            The default value of text is “is cool”
    We must use the option strict_slashes=False in our route
    definition
"""
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


@app.route('/c/<text>', strict_slashes=False)
def print_ctext(text):
    """display “C ” followed by the value
    of the text variable (replace
    underscore _ symbols with a space )
    """
    text = text.replace('_', ' ')
    return ('C' + ' ' + text)


@app.route('/python/(<text>)', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
@app.route('/python', strict_slashes=False)
@app.route('/python/<path:text>', strict_slashes=False)
def print_pythontext(text=None):
    """display “Python ” followed by the value
    of the text variable (replace
    underscore _ symbols with a space )
    """
    if text is None:
        text = 'is cool'
    else:
        text = text.replace('_', ' ')
    return ('Python' + ' ' + text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
