#!/usr/bin/python3
"""
Flask web app that lists states
"""
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.teardown_appcontext
def close_session(r):
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def cities_by_states(state_id=None):
    states = storage.all(State)
    if state_id is None:
        states = states.values()
    else:
        key = "State.{}".format(state_id)
        if key in states:
            states = [states[key]]
        else:
            states = []
    return render_template("9-states.html", states=states, state_id=state_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
