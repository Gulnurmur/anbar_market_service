from .base import Config
from datetime import timedelta
import os

class Development(Config):

    SQLALCHEMY_DATABASE_URI = "postgres:///flask_market"

    DEVELOPMENT = True
    ASSETS_DEBUG = True
    DEBUG = True