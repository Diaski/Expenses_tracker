from flask import Flask
from .extensions import db

app = Flask(__name__)
def create_app()->Flask:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
    app.secret_key='wchujtajnyklucz'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
