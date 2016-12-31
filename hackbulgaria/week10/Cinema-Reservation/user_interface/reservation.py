import sqlite3
from queries.manage_db_queries import *
from user_interface.movie import show_movies
from user_interface.projection import show_projections
from user_interface.availability import check_available

def make_reservation(user, password):

    db = sqlite3.connect(DB_NAME)
    c = db.cursor()

    print('Hello, {0}'.format(user))
    num_tickets = input('Step 1 (User): Choose number of tickets> ')
    try:
        if int(num_tickets) <= 0:
            print('Invalid input for Step 1 !')
            return
    except:
        print('Invalid input for Step 1 !')
        return 
    _movies = show_movies(c)
    movie_chosen = input('Step 2 (Movie): Choose a movie> ')
    _proj = show_projections(c, movie_chosen)
    projection_chosen = input('Step 3 (Projection): Choose a projection> ')
    check_available(c, projection_chosen)
    check = 1
    all_sits = []
    while check <= int(num_tickets):
        sit = input('Step 4 (Seats): Choose seat {0}>'.format(check))
        run_availbl = check_available(c, projection_chosen, sit, user)
        if run_availbl:
            db.commit()
            print('One reservation done !')
            check += 1
            all_sits.append(run_availbl)
        else:
            print('Invalid input for step(4)!')
            continue
    print('This is your reservation:')
    print('Movie: ', _movies)
    print('Date and Time: ', _proj)
    for i in all_sits:
        print(i, end=" ")
    print()
    final = input('Step 5 (Confirm - type "finalize") >')
    print('Thanks.')
    
    
    
                    
            
            
