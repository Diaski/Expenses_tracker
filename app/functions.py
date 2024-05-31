from .models import User,Expense
import base64
import uuid
import hashlib
from .extensions import db

def db_add(val:object) -> None:
    db.session.add(val) 
    db.session.commit()
    db.session.refresh(val)

def register(username:str, password:str) -> str:
    if not username or not password:
        return "Username and password required"
    salt= base64.urlsafe_b64encode(uuid.uuid4().bytes)
    hashed_password=hash_password(password, salt)
    newuser = User(username=username,salt=salt, password=hashed_password)
    db_add(newuser)
    return 'done'

def add_expense(amount:float, description:str, user_id:int) -> str:
    if not amount:
        return "Amount required"
    newexpense = Expense(amount=amount, description=description, user_id=user_id)
    db_add(newexpense)
    return 'done'

def show_expenses() -> tuple:
    userid=1
    user=User.query.get(userid)
    expenses=Expense.query.filter_by(user_id=userid).all()
    return expenses,user

def login(username:str, password:str) -> str:
    user=User.query.filter_by(username=username).first()
    if not user:
        return "User not found"
    hashed_password=hash_password(password, user.salt)
    if user.password!=hashed_password:
        return "Wrong password"
    return 'done'

def hash_password(password:str, salt:str) -> str:
    t_sha = hashlib.sha512()
    t_sha.update(password.encode() + salt) 
    return t_sha.hexdigest()