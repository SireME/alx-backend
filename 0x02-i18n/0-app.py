"""
This module is a simple flask app setup with a single route
"""
from flask import Flask, render_template
from flask.wrappers import Response

app: Flask = Flask(__name__)


@app.route("/")
def index() -> Response:
    """
    default route for app
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
