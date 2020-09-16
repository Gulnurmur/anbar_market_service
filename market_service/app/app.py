from flask import Flask
import os, sys
from app.config.settings.extensions import db,flask_uuid,ma
from flask_migrate import Migrate
from app.controller.market import market
from app.models.model import Product,Category




settings = {
    "prod": "config.production.Prodcution",
    "dev": "config.development.Development",
}


def get_settings(settings_name):
    if settings.get(settings_name):

        return settings.get(settings_name)
    raise Exception("Setting name you select %s isn't supported" % settings_name)


def create_app(settings_name):

    app = Flask(__name__)

    settings_obj = get_settings(settings_name)

   
    
    app.register_blueprint(market,url_prefix="/")
    app.config.from_object(settings_obj)
    
    ma.init_app(app)
    db.init_app(app)
    flask_uuid.init_app(app)
     

    Migrate(app,db)

    return app