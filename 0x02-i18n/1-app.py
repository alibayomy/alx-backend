#!/usr/bin/env python3
'''Task 0: Basic Flask app
'''

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ class that has a LANGUAGES class
    attribute equal to ["en", "fr"]."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()


@app.route("/")
def index():
    """Render the home page"""
    return render_template('0-index.html',)


if __name__ == "__main__":
    app.run(debug=True)
