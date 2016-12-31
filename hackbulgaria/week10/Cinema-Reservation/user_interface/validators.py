import hashlib
from functools import wraps
from queries.manage_db_queries import *
from user_interface.custom_exceptions import *

import sqlite3
db =sqlite3.connect(DB_NAME)
c = db.cursor()

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
        user_and_pass = argv # 0 argument is self !!!
        all_users = c.execute(SELECT_ALL_USERS).fetchall()
        if (user_and_pass[1],) not in all_users:
            raise UsernameError('No user with this name !')
        all_passwords = c.execute(SELECT_ALL_PASSWORDS).fetchall()
        if (user_and_pass[2],) not in all_passwords:
            raise PasswordError('Invalid Password!')   
        return func(*argv)
    return wrapper
    
#def check_password(func):
#    @wraps(func)
#    def wrapper(*argv):
#        user_and_pass = func(*argv)
#        all_passwords = c.execute(SELECT_ALL_PASSWORDS).fetchall()
#        if (user_and_pass[1],) not in all_passwords:
#            raise ValueError('Invalid Password!')    
#        return user_and_pass
#    return wrapper
    
def hash_password(func):
    @wraps(func)
    def wrapper(*argv):
        user_and_pw = func(*argv)
        return user_and_pw[0], hide_password(user_and_pw[1])
    return wrapper    

def validate_password(func):
    @wraps(func)
    def wrapper(*argv):
        return func(*argv)
    return wrapper
    
def log_info(func):
    @wraps(func)
    def wrapper(*argv):
        return func(*argv)
    return wrapper
    
    
    
    
    
    
