from queries.manage_db_queries import *

# Show Movies
def show_movies(cursor):
    print('Current movies:')
    all_movies = cursor.execute(MOVIES_ORDERED_BY_RATING).fetchall()
    for i in range(len(all_movies)):
        print('[{0}] - {1} ({2})'.format(all_movies[i][0], 
                                         all_movies[i][1], 
                                         all_movies[i][2]))
    return all_movies                                                 
