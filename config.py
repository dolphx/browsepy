import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "989eCLFOI23AHjD4"

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'metadata.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

