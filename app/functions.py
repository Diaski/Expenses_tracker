from .models import User, Expense
import base64
import uuid
import re 
from flask import flash
from .extensions import db
class _DB:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            return cls._instance
        return cls._instance
    
    def __init__(self):
        super().__init__()
        self.__refresh = self.__refresh

    def __refresh(self,val: object) -> None:
        db.session.commit()
        db.session.refresh(val)

    def add(self,val: object) -> None:
        db.session.add(val)
        self.__refresh(val)

    def delete(self,user_id: int) -> None:
        user = self.get_user(id=user_id)
        if user:
            db.session.delete(user)
            self.__refresh(user)

    def get_user(self,username: str = None, id: int = None) -> object:
        if username:
            return User.query.filter_by(username=username).first()
        if id:
            return User.query.filter_by(id=id).first()

    def get_expense(self,user_id: int = None, id: int = None) -> object:
        if user_id:
            return Expense.query.filter_by(user_id=user_id).all()
        if id:
            return Expense.query.filter_by(id=id).first()

class FuncsUser:
    @staticmethod
    def get_user(username: str) -> object:
        db_instance = _DB()
        return db_instance.get_user(username=username)
    
    @staticmethod
    def get_expense_and_user(user_id: int = None) -> tuple:
        db_instance = _DB()
        return db_instance.get_expense(user_id=user_id), db_instance.get_user(id=user_id)
    
    @staticmethod
    def register(username: str, password: str) -> str:
        db_instance = _DB()
        if db_instance.get_user(username=username):
            return "Username in use"
        salt = base64.urlsafe_b64encode(uuid.uuid4().bytes)
        hashed_password = InsideFuncs.hash_password(password, salt)
        new_user = User(username=username, salt=salt, password=hashed_password)
        db_instance.add(new_user)
        return 'done'
    @staticmethod
    def get_expenses(user_id: int) -> tuple:
        user = User.query.get(user_id)
        expenses = Expense.query.filter_by(user_id=user_id).all()
        return expenses, user

    @staticmethod
    def login(username: str, password: str) -> str:
        user = User.query.filter_by(username=username).first()
        if not user:
            return "User not found"
        hashed_password = InsideFuncs.hash_password(password, user.salt)
        if user.password != hashed_password:
            return "Wrong password"
        return 'done'


class InsideFuncs:
    @staticmethod
    def hash_password(password: str, salt: bytes) -> str:
        import hashlib
        t_sha = hashlib.sha512()
        t_sha.update(password.encode() + salt)
        return t_sha.hexdigest()
class Validate():
    @staticmethod
    def register(username:str,password:str) -> bool:
        USERNAME_REGEX = r'^[a-zA-Z0-9_-]{5,24}$'
        PASSWORD_REGEX = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        if not re.match(USERNAME_REGEX, username):
            flash('Invalid username. Username must be 5-24 characters long and contain only letters, numbers, underscores, and hyphens.')
            return False
        if not re.match(PASSWORD_REGEX, password):
            flash('Invalid password. Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character.')
            return False
        return True
class DataCreation:
    @staticmethod
    def create_expense(amount: float, description: str, user_id: int, currency: str, expense_type: str) -> str:
        db_instance = _DB()
        if not amount:
            return "Amount required"
        new_expense = Expense(amount=amount, description=description, user_id=user_id, currency=currency, type=expense_type)
        db_instance.add(new_expense)
        return 'done'
