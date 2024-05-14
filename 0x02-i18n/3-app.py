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
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Retrieves the locale for a web page."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """Render the home page"""
    return render_template('0-index.html',)


if __name__ == "__main__":
    app.run(debug=True)
