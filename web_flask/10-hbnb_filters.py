
#!/usr/bin/python3
"""
a script that starts a Flask web application:
"""
from flask import Flask
from sys import argv
from flask import render_template
from models import storage


app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters(id_num=None):
    """display html page"""
    state = storage.all("State")
    if id_num is not None and "State.{}".format(id_num) not in state:
        state = None
    return render_template('10-hbnb_filters.html',
                           state=state,
                           id_num=id_num,
                           amenity = storage.all("Amenity"))

@app.teardown_appcontext
def teardown(err):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
