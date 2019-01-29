#!/usr/bin/python3
"""
a script that starts a Flask web application:
"""
from flask import Flask
from sys import argv
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """display message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display message"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """display message"""
    return "C {:s}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """display message"""
    return "Python {:s}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """display a number"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template__n(n):
    """display html page"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even__n(n):
    """display html page"""
    return render_template('6-number_odd_or_even.html', number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
