#!/usr/bin/python3
"""Starts a Flask web application: /: display "Hello HBNB!" /hbnb: dispaly "HBNB"
    /c/<text>: display "C " followed by the value of the text variable
"""
from flask import Flask

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

# Make it listen to other machines
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
