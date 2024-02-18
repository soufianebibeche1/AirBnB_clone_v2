#!/usr/bin/python3
""" module starts a Flask Web application """
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """Flask hello world"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Add Path for URL"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
