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
    """Add Path To URL"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """Creating a Rule"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': "is cool"})
@app.route('/python/<text>')
def python_text(text):
    """Affect the Rule with a Variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>')
def number_route(n):
    """Make The Rule accept Only the number"""
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
