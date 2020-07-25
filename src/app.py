"""
API layer for simple key-word analysis project
"""

from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = FlaskAPI(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from models import Jobs, JobResults


@app.route("/", methods=["GET"])
def hello_world():
    """
    Temp hello world
    """
    return "Hello World"


if __name__ == "__main__":
    app.run()
