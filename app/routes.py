from flask import Blueprint,render_template,request,redirect
from .functions import add_user,show_users,show_expenses


main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Hello, World!"

@main.route('/users')
def list_users():
    return show_users()

@main.route('/expenses')
def list_expenses():
    return show_expenses()

@main.route('/create_user')
def create_user_render_template():
    return render_template('create_user.html')

@main.route('/create_user', methods=['POST'])
def create_user_post():
    username = request.form.get('username')
    password = request.form.get('password')
    response=add_user(username, password)
    if response=="done":
        return redirect('/')
    return render_template('create_user.html', messages=[response])
