#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbtn():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbtn():
    return "HBNB"

if __name__ == "__main__":
    app.run(debug=True)
