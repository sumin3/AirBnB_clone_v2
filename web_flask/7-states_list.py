#!/usr/bin/python3
"""
a script that starts a Flask web application:
"""
from flask import Flask
from sys import argv
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display html page"""
    return render_template('7-states_list.html', state=storage.all("State"))


@app.teardown_appcontext
def teardown(err):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
