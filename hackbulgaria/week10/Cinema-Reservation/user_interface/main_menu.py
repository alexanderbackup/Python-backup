from user_interface.interface import CinemaInterface

user = None
password = None

while True:
    answer = input()
    foo = CinemaInterface()
    if answer == 'show movies':
        print('Current movies:')
        foo._show_movies()
        
    elif 'show movie projections' in answer and answer != 'show movie projections': # <movie_id> [<date>]
        foo._show_projections(answer)
        
    elif answer == 'make reservation':
        if user and password:
            print('??????')
            foo._make_reservation(user, passowrd)
        else:
            log_info = foo._log_user() # has to be tuple !
            user = log_info[0]
            password = log_info[1]
        
    elif answer == 'cancel reservation': # <name>
        pass
        
    elif answer == 'exit':
        foo._exit()
        
    elif answer == 'help':
        pass
        
    else:
        print('Invalid Input!\nTip: Try typing "help".')
