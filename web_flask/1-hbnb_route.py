#!/usr/bin/python3
"""
a script that starts a Flask web application:
1. Your web application must be listening on 0.0.0.0, port 5000
2. Routes: / - display “Hello HBNB!”, /hbnb: display “HBNB”
3. You must use the option strict_slashes=False in your route definition
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """display message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display message"""
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
