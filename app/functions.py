from .models import User,Expense
import base64
import uuid
from .charts import *
from .extensions import db
class DB():
    def refresh(val:object)->None:
        db.session.commit()
        db.session.refresh(val)
    def add(val:object) -> None:
        db.session.add(val) 
        DB.refresh(val)
    def delete(id:int) -> None :
        user=DB.GetUser(id=id)
        db.session.delete(user)
        DB.refresh
    def GetUser(username : str = None ,  id : int = None ) -> object:
        if username != None: return User.query.filter_by(username=username).first()
        if id != None: return User.query.filter_by(id=id).first()
    def GetExpense(user_id : int = None , id : int = None) -> object:
        if user_id!=None : return Expense.query.filter_by(user_id=user_id).all()
        if id !=None : return Expense.query.filter_by(id=id).first()
    def getExpenseAndUser(user_id:int = None) -> tuple:return DB.GetExpense(user_id=user_id),DB.GetUser(id=user_id)

class FuncsUser():

    def register(username:str, password:str) -> str:
        if DB.GetUser(username=username) != None:
            return "Username in use"
        if not username or not password:
            return "Username and password required"
        salt= base64.urlsafe_b64encode(uuid.uuid4().bytes)
        hashed_password=inside_funcs.hash_password(password, salt)
        newuser = User(username=username,salt=salt, password=hashed_password)
        DB.add(newuser)
        return 'done'
    
    def get_expensions(userid) -> tuple:
        user=User.query.get(userid)
        expenses=Expense.query.filter_by(user_id=userid).all()
        return expenses, user
    
    def login(username:str, password:str) -> str:
        user=User.query.filter_by(username=username).first()
        if not user:
            return "User not found"
        hashed_password=inside_funcs.hash_password(password, user.salt)
        if user.password!=hashed_password:
            return "Wrong password"
        return 'done'
  
    def logout_user() -> None:
        from flask import session
        session.pop('user_id', None)   
class DataCreation():
    def create_expense(amount:float, description:str, user_id:int, currency:str, expense_type:str) -> str:
            if not amount:
                return "Amount required"
            newexpense = Expense(amount=amount, description=description, user_id=user_id,currency=currency,type=expense_type)
            DB.add(newexpense)
            return 'done'

class inside_funcs():
    def hash_password(password:str, salt:bytes) -> str:
        import hashlib
        t_sha = hashlib.sha512()
        t_sha.update(password.encode() + salt) 
        return t_sha.hexdigest()

