#!/usr/bin/python3

"""
 a script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State

states = storage.all(State)
app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
     remove the current SQLAlchemy Session after each request
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state_list():
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    return render_template('7-states_list.html', objects=sorted_states)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
