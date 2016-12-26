from queries.manage_db_queries import *

# Show Movies
def show_movies(cursor):
    all_movies = cursor.execute(MOVIES_ORDERED_BT_RATING).fetchall()
    for i in range(len(all_movies)):
        print('[{0}] - {1} ({2})'.format(i, 
                                         all_movies[i][0], 
                                         all_movies[i][1]))
                                                 
