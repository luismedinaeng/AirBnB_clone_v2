#!/usr/bin/python3
"""
Web application that responds to hbnb_filters
"""
from flask import Flask, render_template
from models import storage, State, Amenity

app = Flask(__name__)
app.url_map.strict_slashes=False

@app.route('/hbnb_filters')
def hbnb_filters():
    """
    Responds to the '/hbnb_filters' dir
    """
    states = storage.all(State).values()
    amen = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amen)

@app.teardown_appcontext
def close_conn(e):
    """
    Function after making the request
    """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
