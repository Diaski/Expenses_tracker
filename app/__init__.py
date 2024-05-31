from flask import Flask, redirect, url_for, session,request
from .extensions import db
from . import config

app = Flask(__name__)
def create_app()->Flask:
    app.config.from_object(config.DevelopmentConfig)
    db.init_app(app)


    @app.before_request
    def check_session():
        allowed_endpoints = ['login_post','login', 'create_user','create_user_post','home']

        if 'user_id' not in session:
            if request.endpoint not in allowed_endpoints and not request.endpoint.startswith('static'):
                return redirect(url_for('login'))

        if 'user_id' in session:
            session.permanent = True
        
    with app.app_context():
        db.create_all()
    return app
