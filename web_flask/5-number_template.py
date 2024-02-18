#!/usr/bin/python3
""" module starts a Flask Web application """
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """Flask hello world"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Add path To URL"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """Create a Flask Rule"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': "is cool"})
@app.route('/python/<text>')
def python_text(text):
    """Give The Rule a Value"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>')
def number_route(n):
    """Let The Rule Accept Only Numbers"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:number>')
def number_template(number):
    """create an html page with a Rule"""
    return render_template('5-number.html', number=number)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
