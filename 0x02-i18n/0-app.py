"""
This module is a simple flask app setup with a single route
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """
    default route for app
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
