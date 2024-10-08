#!/usr/bin/env python3
"""Flask app module for flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Function that defines the page for / route
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
