import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///lms.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False