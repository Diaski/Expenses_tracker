from .views import home,create_expense, create_expense_post,login,register,register_post
from flask import Flask
def add_url(app:Flask)->Flask:
    app.add_url_rule('/', 'home', home)
    app.add_url_rule('/register', 'create_user', register)
    app.add_url_rule('/register', 'create_user_post', register_post, methods=['POST'])
    app.add_url_rule('/create_expense', 'create_expense', create_expense)
    app.add_url_rule('/create_expense', 'create_expense_post', create_expense_post, methods=['POST'])
    app.add_url_rule('/login', 'login', login)
    return app


