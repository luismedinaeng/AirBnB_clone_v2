#!/usr/bin/python3
"""
Deploy a Flask app for Airbnb clone
"""
from flask import Flask, render_template
from models import storage, State, Amenity, Place

app = Flask(__name__)
app.url_map.strict_slashes=False

@app.route('/hbnb')
def hbnb():
    """
    Respond to '/hbnb' request
    """
    states = storage.all(State).values()
    amen = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template("100-hbnb.html", states=states,
                           amenities=amen, places=places)

@app.teardown_appcontext
def close_storage(e):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
