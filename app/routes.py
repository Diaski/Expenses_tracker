from .views import render,post,funcs
from flask import Flask

def add_url(app:Flask) -> Flask:
    app.add_url_rule('/', 'home', render.home)
    app.add_url_rule('/register', 'create_user', render.register)
    app.add_url_rule('/register', 'create_user_post', post.register, methods=['POST'])
    app.add_url_rule('/create_expense', 'create_expense', render.create_expense)
    app.add_url_rule('/create_expense', 'create_expense_post', post.create_expense, methods=['POST'])
    app.add_url_rule('/login', 'login', render.login)
    app.add_url_rule('/login', 'login_post', post.login, methods=['POST'])
    app.add_url_rule('/dashboard', 'dashboard', render.dashboard)
    app.add_url_rule('/logout', 'logout', funcs.logout)
    app.add_url_rule('/view_expenses', 'view_expenses', render.expenses)
    app.add_url_rule('/view_charts', 'view_charts', render.charts)
    
    return app


