import hashlib
from functools import wraps
from queries.manage_db_queries import DB_NAME, SELECT_ALL_PASSWORDS


def hide_password(password):
    hash_object = hashlib.sha512(password.encode())
    return hash_object.hexdigest()

def atomic(func):
    @wraps(func)
    def wrapper(*argv):
        return func(*argv)
    return wrapper
    
def user_exists(func):
    @wraps(func)
    def wrapper(*argv):
        return func(*argv)
    return wrapper
    
def validate_password(func):
    @wraps(func)
    def wrapper(*argv):
        # TODO: Check if I need sqlite3 anywhere ewse here and move it up !
        import sqlite3
        db =sqlite3.connect(DB_NAME)
        c = db.cursor()
        user_and_pass = func(*argv)
        all_passwords = c.execute(SELECT_ALL_PASSWORDS).fetchall()
        if (user_and_pass[1],) not in all_passwords:
            raise ValueError('Invalid Password!')    
        return user_and_pass
    return wrapper
    
def hash_password(func):
    @wraps(func)
    def wrapper(*argv):
        user_and_pw = func(*argv)
        return user_and_pw[0], hide_password(user_and_pw[1])
    return wrapper    

def log_info(func):
    @wraps(func)
    def wrapper(*argv):
        return func(*argv)
    return wrapper
    
    
    
    
    
    
