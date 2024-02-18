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
    """Add Path For URL"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """Flask Variable Rule"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/<text>')
def python_text(text="is cool"):
    """Instatiate Rule with a Default Value"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
