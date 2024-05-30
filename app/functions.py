from .models import User,Expense
from .extensions import db
def show_users():
    users=User.query.all()
    return (user.username+"<br>" for user in users)
def show_expenses():
    expenses=Expense.query.all()
    return (expense.description for expense in expenses)
def add_user(username, password) :
    if not username or not password:
        return "Username and password required"
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    db.session.refresh(newuser)
    return 'done'