import hashlib
from functools import wraps
import string

def hash_password(func):
    @wraps(func)
    def wrapper(*argv):
        user, password = argv[0], argv[1]
        hash_object = hashlib.sha512(password.encode())
        return func(user, hash_object.hexdigest())
    return wrapper

def validate_password(func):
    def wrapper(*argv):
        user, pw = argv[0], argv[1]
        # check length and username in pw
        if (len(pw) < 8) or (str(user) in pw):
            raise PasswordError()
        # check for uppercase
        if len(set(string.ascii_uppercase).intersection(pw)) < 1:
            raise PasswordError()
        # check for special symbol
        if len(set(string.punctuation).intersection(pw)) < 1:
            raise PasswordError()    
        return func(user, pw)
    return wrapper
    
class PasswordError(Exception):
    pass   
    

# More then 8 symbols
# Must have capital letters, and numbers and a special symbol
# Username is not in the password (as a substring)

