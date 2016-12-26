from caesarCipher import CaesarCypther
import datetime
import logging
from functools import wraps

def log(file_name):
    def _log(func):  
        logging.basicConfig(filename=file_name, level=logging.INFO)
        @wraps(func)
        def wrapper(*args, **kwargs):
            logging.info('{0} was called at {1}'.format(
                                func.__name__,
                                str(datetime.datetime.now()))
                                                        )
                                                        
            return func()
        return wrapper
    return _log

def encrypt(key):    
    def decorate_func(func):
        foo = CaesarCypther(key, func(1))
        foo.encipher()
        result = foo.result
        @wraps(func)
        def wrapper():
            return result
        return wrapper
    return decorate_func


@log('log.txt')
@encrypt(2)
def get_low(a):
    return "Get get get low"

print(get_low(1))

