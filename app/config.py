import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:PASSWORD@database-2.cdecyo464bcu.ap-south-1.rds.amazonaws.com:3306/lms'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
