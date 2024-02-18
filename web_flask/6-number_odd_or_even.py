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
    """Add Path To URL"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """Create A Rule"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': "is cool"})
@app.route('/python/<text>')
def python_text(text):
    """Give The Rule A Value"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>')
def number_route(n):
    """imake Rule Accept only Numbers"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:number>')
def number_template(number):
    """create an html page with a rule"""
    return render_template('5-number.html', number=number)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Create a template with 2 variables"""
    odd_even = "even" if (n % 2 == 0) else "odd"
    return render_template("6-number_odd_or_even.html",
                           number=n, odd_even=odd_even)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
