"""
Configuration class.
Currently no environment segmentation.
"""
import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ["KEY_PHRASE_DB_URL"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
