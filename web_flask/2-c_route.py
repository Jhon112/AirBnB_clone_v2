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


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return "C {}".format(text.replace("_", " "))

if __name__ == "__main__":
    app.run(debug=True)
