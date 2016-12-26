import sqlite3
from random import choice
from queries.manage_db_queries import *
from settings.sql_creation_settings import *

db = sqlite3.connect(DB_NAME) # DB_NAME = '
c = db.cursor()

def create_tables():
    # Check if tables already exist
    c.execute(DROP_MOVIES_TABLE)
    c.execute(DROP_PROJECTIONS_TABLE)
    c.execute(DROP_USERS_TABLE)
    c.execute(DROP_RESERVATIONS_TABLE)
    db.commit()

    # Create new tables
    c.execute(CREATE_MOVIES_TABLE)
    c.execute(CREATE_PROJECTIONS_TABLE)
    c.execute(CREATE_USERS_TABLE)
    c.execute(CREATE_RESERVATIONS_TABLE)
    db.commit()

def populate_tables():
            
    users = choice(ALL_USERS)
    
    c.executemany(INSERT_INTO_USERS, users)
    db.commit()
    
    movies = choice(ALL_MOVIES)
             
    c.executemany(INSERT_INTO_MOVIES, movies)
    db.commit()
    
    projections = choice(ALL_PROJECTIONS)
                 
    c.executemany(INSERT_INTO_PROJECTIONS, projections)
    db.commit()
    
    reservations = choice(ALL_RESERVATIONS)
                 
    c.executemany(INSERT_INTO_RESERVATIONS, reservations)
    db.commit()   

create_tables()
populate_tables()


