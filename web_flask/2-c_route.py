#!/usr/bin/python3
"""
a script that starts a Flask web application:
1. Your web application must be listening on 0.0.0.0, port 5000
2. Routes: / - display “Hello HBNB!”, /hbnb: display “HBNB”
3. /c/<text>: display “C ” followed by the value of the tex
variable (replace underscore _ symbols with a space )
"""
from flask import Flask
from sys import argv
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
