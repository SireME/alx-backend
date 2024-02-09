#!/usr/bin/env python3
"""
Basic Flask app with basic i18n configs
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    default configs for babel
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """
    determine best match for users preferrred lanaguage
    """
    rq = request.accept_languages
    return rq.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Route for the root URL."""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
