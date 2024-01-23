#!/usr/bin/python3
"""Starts a Flask web application: /: display "Hello HBNB!" /hbnb: dispaly "HBNB"
    /c/<text>: display "C " followed by the value of the text variable
"""
from flask import Flask, render_template

# Starting the application
app = Flask(__name__)

# Routing to the path '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return hello_hbnb"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return HBNB"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """Display 'C ' followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Display python + value of the text"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display {num} + is a number"""
    if type(n) is int:
        return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def html_diplay(n):
    """Display render HTML page if n is an integer"""
    n = str(n)
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def html_odd_even(n):
    """Display render HTML page if n is an odd|even"""
    return render_template('6-number_odd_or_even.html', n=n)

# Make it listen to other machines
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
