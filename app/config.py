import os


class ConfigDevelopment():
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'
    SQLALCHEMY_TRACK_NOTIFICATION = False
    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True

class ConfigProduction:
    SQLALCHEMY_DATABASE_URI = 'postgresql://flask:flask@pg:5432/flask'
    SQLALCHEMY_TRACK_NOTIFICATION = False
    FLASK_ENV = 'production'
    TESTING = False
    DEBUG = False

if os.environ.get("FLASK_ENV") == "production":
    config = ConfigProduction()
else:
    config = ConfigDevelopment()

