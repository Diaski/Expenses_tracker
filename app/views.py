from flask import render_template, request, redirect, url_for, session,flash
from .functions import FuncsUser,DataCreation,Validate
from flask.typing import TemplateGlobalCallable
class Render():
        
    @staticmethod
    def home() -> TemplateGlobalCallable: 
        return render_template('home.html')
    
    @staticmethod
    def login() -> TemplateGlobalCallable : 
        return render_template('login.html')
    
    @staticmethod
    def register() -> TemplateGlobalCallable: 
        return render_template('register.html')
    
    @staticmethod
    def create_expense() -> TemplateGlobalCallable: 
        return render_template('create_expanses.html')
    
    @staticmethod
    def dashboard() -> TemplateGlobalCallable:
        if 'user_id' in session:
            user_id = session['user_id']
            session.permanent = True
            expenses,user= FuncsUser.get_expense_and_user(user_id=user_id)
            return render_template('dashboard.html', user=user, expenses=expenses)
        else:
            return redirect(url_for('login'))
            
    @staticmethod
    def expenses() -> str:
        user_id=session['user_id']
        session.permanent = True
        expenses, user = FuncsUser.get_expense_and_user(user_id=user_id)
        return render_template('user_expenses.html', user=user, expenses=expenses)
        
    @staticmethod
    def charts() -> TemplateGlobalCallable:
        user_id=session['user_id']
        plot_url=(user_id)
        session.permanent = True
        return render_template('charts.html', plot_url=plot_url)
    
class Post():
    @staticmethod
    def register () -> TemplateGlobalCallable:
        username = request.form.get('username')
        password = request.form.get('password')
        valid=Validate.register(username, password)
        if not valid:
            return render_template('register.html')
        response=FuncsUser.register(username, password)
        if response=="done":
            return redirect('/')
        flash(response, 'error')
        print(response)
        return render_template('register.html', messages=[response])
        
    @staticmethod
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
    
    @staticmethod
    def login() -> TemplateGlobalCallable:
        username = request.form.get('username')
        password = request.form.get('password')
        response=FuncsUser.login(username, password)
        if response=="done":
            user = FuncsUser.get_user(username=username)
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('dashboard'))
        flash(response,'error')
        return render_template('login.html')

class Funcs():    
    @staticmethod
    def logout() -> TemplateGlobalCallable:
        session.pop('user_id', None)  
        return redirect(url_for('home'))
