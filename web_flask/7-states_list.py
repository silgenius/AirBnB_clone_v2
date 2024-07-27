#!/usr/bin/python3

"""
 a script that starts a Flask web application
"""

from flask import Flask
from models import storage
from models import State

objects = storage.all(State)
app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext():
    """
     remove the current SQLAlchemy Session after each request
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state_list():
    return render_template('7-states_list.html', objects=objects)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
