from datetime import timedelta
from .extensions import get_key

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///expenses.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = get_key()
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
