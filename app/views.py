from flask import render_template,request,redirect,flash
from .functions import register,add_expense,login
from typing import Callable


def home() -> Callable : return render_template('home.html')

def register() -> Callable: return render_template('register.html')

def register_post () -> Callable:
    username = request.form.get('username')
    password = request.form.get('password')
    response=register(username, password)
    if response=="done":
        return redirect('/')
    flash(response)
    return render_template('create_user.html', messages=[response])

def create_expense() -> Callable: return render_template('create_expanses.html')

def create_expense_post() -> Callable:
    amount = request.form.get('amount')
    description = request.form.get('description')
    user_id=1
    response=add_expense(amount, description, user_id)
    if response=="done":
        return redirect('/')
    flash(response,'error')
    return render_template('create_expanses.html')

def login() -> Callable : return render_template('login.html')

def login_post() -> Callable:
    username = request.form.get('username')
    password = request.form.get('password')
    response=login(username, password)
    if response=="done":
        return redirect('/')
    flash(response,'error')
    return render_template('login.html')

