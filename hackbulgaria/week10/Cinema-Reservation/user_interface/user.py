from user_interface.validators import *
from getpass import getpass


def log_user():
    print('You need to log the user in the system to make reservations!')
    username = input('Username: ')
    password = getpass()
    
    return(username, password)

