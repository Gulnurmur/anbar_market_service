from .base import Config
from datetime import timedelta
import os

class Development(Config):

    SQLALCHEMY_DATABASE_URI = "postgres:///flask_anbar"

    DEVELOPMENT = True
    ASSETS_DEBUG = True
    DEBUG = True