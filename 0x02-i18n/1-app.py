#!/usr/bin/env python3
'''Task 0: Basic Flask app
'''

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
app.config.


@app.route("/")
def index():
    """Render the home page"""
    return render_template('0-index.html',)


if __name__ == "__main__":
    app.run(debug=True)
