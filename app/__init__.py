from flask import Flask
from .extensions import db
from .config import DevelopmentConfig

def create_app(config_class=DevelopmentConfig) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
                
    with app.app_context():
        db.create_all()

    return app


   