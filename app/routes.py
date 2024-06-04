from flask import Flask
from .views import Render, PostFuncs, Funcs

def add_url(app: Flask) -> Flask:
    app.add_url_rule('/', 'home', Render.home)
    app.add_url_rule('/register', 'create_user', Render.register)
    app.add_url_rule('/register', 'create_user_post', PostFuncs.register, methods=['POST'])
    app.add_url_rule('/create_expense', 'create_expense', Render.create_expense)
    app.add_url_rule('/create_expense', 'create_expense_post', PostFuncs.create_expense, methods=['POST'])
    app.add_url_rule('/login', 'login', Render.login)
    app.add_url_rule('/login', 'login_post', PostFuncs.login, methods=['POST'])
    app.add_url_rule('/dashboard', 'dashboard', Render.dashboard)
    app.add_url_rule('/logout', 'logout', Funcs.logout)
    app.add_url_rule('/view_expenses', 'view_expenses', Render.expenses)
    
    return app