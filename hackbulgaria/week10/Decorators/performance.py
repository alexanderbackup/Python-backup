from time import sleep, time
import logging
from functools import wraps


def performance(file_name):
    def _performance(func):
        logging.basicConfig(filename=file_name, level=logging.INFO)
        t1 = time()
        res = func()
        t2 = time() - t1
        @wraps(func)
        def wrapper():
            logging.info('{0} was called and took {1} seconds to complete'.format(func.__name__, t2))
            return func
        return wrapper            
    return _performance
                                
@performance('log.txt')
def something_heavy():
    sleep(2)
    return "I am done!"

something_heavy()

#I am done!                                
