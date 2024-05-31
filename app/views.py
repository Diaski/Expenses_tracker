from flask import Flask, render_template, request, redirect, url_for, session,flash
from .functions import register,add_expense,login,show_expenses,get_user_by_username,charts
from typing import Callable


def home() -> Callable : return render_template('home.html')

def register_render() -> Callable: return render_template('register.html')

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
    user_id=session['user_id']
    currency = request.form.get('currency')
    expense_type = request.form.get('expense_type')
    response=add_expense(amount, description, user_id,currency,expense_type)
    if response=="done":
        return redirect('/dashboard')
    flash(response,'error')
    return render_template('create_expanses.html')

def login_render() -> Callable : return render_template('login.html')

def login_post() -> Callable:
    username = request.form.get('username')
    password = request.form.get('password')
    response=login(username, password)
    if response=="done":
        user = get_user_by_username(username)
        session['user_id'] = user.id
        return redirect(url_for('dashboard'))
    flash(response,'error')
    return render_template('login.html')
def dashboard() -> Callable:
    if 'user_id' in session:
        user_id = session['user_id']
        expenses, user = show_expenses(user_id)
        return render_template('dashboard.html', user=user, expenses=expenses)
    else:
        return redirect(url_for('login'))
def logout() -> Callable:
    session.pop('user_id', None)
    return redirect(url_for('home'))
def render_expenses() -> str:
    user_id=session['user_id']
    expenses, user = show_expenses(user_id)
    return render_template('user_expenses.html', user=user, expenses=expenses)

def view_charts() -> Callable:

    user_id=session['user_id']
    plot_url=charts(user_id)
    return render_template('charts.html', plot_url=plot_url)