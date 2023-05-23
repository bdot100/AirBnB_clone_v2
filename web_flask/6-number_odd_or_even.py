#!/usr/bin/python3
""" This script starts a Flask web application:
    web application is listening on 0.0.0.0, port 5000
    Routes: 
    /: display “Hello HBNB!”
    /hbnb displays "HBNB"
    /c/<text>: display “C ” followed by the value
    of the text variable (replace underscore _ symbols with
    a space )
    /python/(<text>): display “Python ”, followed
            by the value of the text variable 
            (replace underscore _ symbols with a space )
            The default value of text is “is cool”
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an 
    integer: H1 tag: “Number: n” inside the tag BODY
    /number_odd_or_even/<n>: display a HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY
    We must use the option strict_slashes=False in our route
    definition 
"""
from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def print_number(n):
    """display “n is a number” only if n is an integer"""
    return ('{:d} is a number'.format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def print_template(n):
    """Display a HTML page only if n is an integer:
    """
    return (render_template('5-number.html', n=n))


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def print_odd_even(n):
    """ display a HTML page only if n is an integer:
    """
    return (render_template('6-number_odd_or_even.html', n=n))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
