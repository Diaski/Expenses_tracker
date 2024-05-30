from flask import Flask
from .extensions import db
from .models import User,Expense
from .routes import main

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(main)
    with app.app_context():
        db.create_all()
        '''new_user = User(username='alice', password='password123')
        db.session.add(new_user)
        db.session.commit()
        db.session.refresh(new_user)'''
        '''new_expense = Expense(amount=100.0, description='Pizza', user_id=1)
        db.session.add(new_expense)
        db.session.commit()
        db.session.refresh(new_expense)'''
    return app
