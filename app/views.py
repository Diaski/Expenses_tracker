from flask import Flask, render_template, request, redirect, url_for, session,flash
from flask.typing import TemplateGlobalCallable
from .functions import DB,FuncsUser,DataCreation
from .charts import *



class render():
    def home() -> TemplateGlobalCallable : return render_template('home.html')

    def login() -> TemplateGlobalCallable : return render_template('login.html')

    def register() -> TemplateGlobalCallable: return render_template('register.html')

    def create_expense() -> TemplateGlobalCallable: return render_template('create_expanses.html')

    def dashboard() -> TemplateGlobalCallable:
        if 'user_id' in session:
            user_id = session['user_id']
            session.permanent = True
            expenses,user= DB.getExpenseAndUser(user_id=user_id)
            return render_template('dashboard.html', user=user, expenses=expenses)
        else:
            return redirect(url_for('login'))
        
    def expenses() -> str:
        user_id=session['user_id']
        session.permanent = True
        expenses, user = DB.getExpenseAndUser(user_id=user_id)
        return render_template('user_expenses.html', user=user, expenses=expenses)
    
    def charts() -> TemplateGlobalCallable:
        user_id=session['user_id']
        plot_url=(user_id)
        session.permanent = True
        return render_template('charts.html', plot_url=plot_url)
class post():
    def register () -> TemplateGlobalCallable:
        username = request.form.get('username')
        password = request.form.get('password')
        response=FuncsUser.register(username, password)
        if response=="done":
            return redirect('/')
        flash(response, 'error')
        print(response)
        return render_template('register.html', messages=[response])
    
    def create_expense() -> TemplateGlobalCallable:
        amount = request.form.get('amount')
        description = request.form.get('description')
        user_id=session['user_id']
        currency = request.form.get('currency')
        expense_type = request.form.get('expense_type')
        response=DataCreation.create_expense(amount, description, user_id,currency,expense_type)
        if response=="done":
            return redirect('/dashboard')
        flash(response,'error')
        return render_template('create_expanses.html')
    
    def login() -> TemplateGlobalCallable:
        username = request.form.get('username')
        password = request.form.get('password')
        response=FuncsUser.login(username, password)
        if response=="done":
            user = DB.GetUser(username=username)
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('dashboard'))
        flash(response,'error')
        return render_template('login.html')

class funcs():
    def logout() -> TemplateGlobalCallable:
        session.pop('user_id', None)  
        return redirect(url_for('home'))
