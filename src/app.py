"""
API layer for simple key-word analysis project
"""

from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask_sqlalchemy import SQLAlchemy

from config import Config
from models import db, Jobs, JobResults

app = FlaskAPI(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route("/", methods=["GET"])
def get_job_by_key_phrase():
    """
    Returns job details by provided key_phrase
    """
    current_job = Jobs.query.filter_by(key_phrase='test_phrase').first()
    return str(current_job.creation_timestamp)


if __name__ == "__main__":
    app.run()
