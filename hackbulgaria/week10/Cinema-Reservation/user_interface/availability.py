from queries.manage_db_queries import *        
from copy import deepcopy
from ast import literal_eval


def check_available(cursor, projection_id, chosen_sit=None, user=None):

    # taken_sits = tuple(row, col)
    taken_sits = cursor.execute(
                                SELECT_ALL_TAKEN_SITS,
                                (projection_id)
                               ).fetchall()
    if chosen_sit:
        try:
            valid_sit_cords = literal_eval(chosen_sit) # str => tuple
            if valid_sit_cords[0] > CINEMA_SIZE[0] or valid_sit_cords[1] > CINEMA_SIZE[1]:
                print('Lol...NO!')
                return False
            if valid_sit_cords in taken_sits:
                print('This seat is already taken!')
                return False
            get_user_id = cursor.execute(GET_USER_ID, [(user)]).fetchone()[0]
            smth = (get_user_id,
                    projection_id,
                    valid_sit_cords[0],
                    valid_sit_cords[1])
            cursor.execute(RESERVE_SIT, smth)
            
        except:
            return False
        return valid_sit_cords # valid sits example: tuple(5, 5)
    
    else:
        taken_sits = [(i[0]-1, i[1]-1) for i in taken_sits]
        print(taken_sits)
        cinema = [[True for i in range(CINEMA_SIZE[0])] for i in range(CINEMA_SIZE[1])]
        valid_cords = set()
        for row in range(len(cinema)):
            for col in range(len(cinema[row])):
                valid_cords.add((row, col))
                if (row, col) in taken_sits:
                    cinema[row][col] = False 
                    
        # print cinema sits !
        def pprint_cinema(cinema):
            iter_cinema = [deepcopy(i) for i in cinema]
            print('   1 2 3 4 5 6 7 8 9 10')
            for row in range(len(iter_cinema)):
                row_print = ''
                for col in range(len(iter_cinema[row])):
                    if iter_cinema[row][col]:
                        row_print += ' .'
                    else:
                        row_print += ' X'
                if row+1 <= 9:
                    print(str(row+1) + ' ' + row_print)
                else:
                    print(str(row+1) + row_print)
        pprint_cinema(cinema)


#import sqlite3
#db = sqlite3.connect(DB_NAME)
#c = db.cursor()
#check_available(c, '5', '(5, 5)', 'Eric Cartman')

