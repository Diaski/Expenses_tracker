from .views import Render,Post as post,Funcs
from flask import Flask
def add_url(app:Flask) -> Flask:
    app.add_url_rule('/', 'home', Render.home)
    app.add_url_rule('/register', 'create_user', Render.register)
    app.add_url_rule('/register', 'create_user_post', post.register, methods=['post'])
    app.add_url_rule('/create_expense', 'create_expense', Render.create_expense)
    app.add_url_rule('/create_expense', 'create_expense_post', post.create_expense, methods=['post'])
    app.add_url_rule('/login', 'login', Render.login)
    app.add_url_rule('/login', 'login_post', post.login, methods=['post'])
    app.add_url_rule('/dashboard', 'dashboard', Render.dashboard)
    app.add_url_rule('/logout', 'logout', Funcs.logout)
    app.add_url_rule('/view_expenses', 'view_expenses', Render.expenses)
    app.add_url_rule('/view_charts', 'view_charts', Render.charts)
    
    return app


