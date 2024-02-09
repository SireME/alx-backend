#!/usr/bin/env python3
"""
Basic Flask app with basic i18n configs
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    default configs for babel
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAUL_LOCALE = 'en'
    BABEL_DEFAUL_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """Route for the root URL."""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
