#!/usr/bin/python3
"""
This module starts a Flask apllication.
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """hello world"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """add a path to the url"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """make a simple variable rule"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    # values here are the default, mentioned as keepsake
    app.run(host="0.0.0.0", port="5000")
