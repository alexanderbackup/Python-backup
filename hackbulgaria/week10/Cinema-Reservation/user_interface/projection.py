from queries.manage_db_queries import *

# Show movie projections
def show_projections(cursor, answer):
    ans = answer.replace('show movie projections ', '').split(' ')
    if len(ans) == 1:
        projs = cursor.execute(PROJECTIONS_1_ORDERED_BY_DATE, (ans[0])).fetchall()
        print('Projections for movie ' + projs[0][0] +' :')
        for mov in projs:
            print('[?] - {0} {1} ({2})'.format(mov[1],
                                         mov[2],
                                         mov[3]))
    elif len(ans) == 2:
        projs = cursor.execute(PROJECTIONS_2_ORDERED_BY_DATE, (ans[0], ans[1])).fetchall()
        print('Projections for movie ' + projs[0][0] + ' on date ' + projs[0][1]+ ' :')
        for mov in projs:
            print('[?] - {0} ({1})'.format(mov[2],
                                         mov[3]))            
    else:
        print('SOME ERROR')
        exit(0)
