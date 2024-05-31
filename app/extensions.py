from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def get_key() -> str:
    with open('keyhashed.txt', 'r') as f:
        key=f.read()
    return str(key)