"""
Tables in the key_phrase db
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

db = SQLAlchemy()


class Jobs(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    key_phrase = db.Column(db.String(1000))
    creation_timestamp = db.Column(db.DateTime, server_default=func.now())
    last_run_timestamp = db.Column(db.DateTime, nullable=True)
    single_run_only = db.Column(db.Boolean)
    job_results = relationship("JobResults", back_populates="job")

    def __init__(self, key_phrase, single_run_only):
        self.key_phrase = key_phrase
        self.single_run_only = single_run_only

    def __repr__(self):
        return 'id: %s key_phrase: %s' % (self.id, self.key_phrase)


class JobResults(db.Model):
    __tablename__ = 'job_results'

    job_id = db.Column(db.Integer, ForeignKey('jobs.id'), primary_key=True)
    run_timestamp = db.Column(db.DateTime, primary_key=True, default=datetime.utcnow)
    query_result = db.Column(db.String(1000), primary_key=True)
    positive_count = db.Column(db.Integer)
    negative_count = db.Column(db.Integer)
    neutral_count = db.Column(db.Integer)
    job = relationship("Jobs", back_populates="job_results")

    def __init__(self, job_id, query_result,
                 positive_count, negative_count, neutral_count):
        self.job_id = job_id
        self.query_result = query_result
        self.positive_count = positive_count
        self.negative_count = negative_count
        self.neutral_count = neutral_count

    def __repr__(self):
        return 'id: %s | query result: %s' % (
            self.job_id, self.query_result
        )
