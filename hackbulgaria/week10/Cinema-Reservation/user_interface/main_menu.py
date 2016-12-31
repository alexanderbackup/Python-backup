from user_interface.interface import CinemaInterface
from user_interface.custom_exceptions import *


user_name = None
password = None

while True:
    answer = input()
    foo = CinemaInterface()
    if answer == 'show movies':
        foo._show_movies()
        
    elif 'show movie projections' in answer and answer != 'show movie projections': # <movie_id> [<date>]
        foo._show_projections(answer)

    elif answer == 'make reservation':
        if not user_name and not password:
            log_info = foo._log_user() # has to be tuple !
            user_name = log_info[0]
            password = log_info[1]
            print('<<<So far so gud !>>>') # Eric Cartman 12$C4567
        try:
            foo._make_reservation(user_name, password)
        except(UsernameError, PasswordError) as e:
            print(e)
            print('Please try again !')
            user_name = None
            password = None
            continue
            
    elif answer == 'cancel reservation': # <name>
        pass
        
    elif answer == 'exit':
        foo._exit()
        
    elif answer == 'help':
        pass
        
    else:
        print('Invalid Input!\nTip: Try typing "help".')
