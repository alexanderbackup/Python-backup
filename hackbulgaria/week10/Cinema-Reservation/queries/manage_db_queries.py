# database name
DB_NAME = 'queries/cinema.db'

# cinema size

CINEMA_SIZE = (10, 10)

# create tables

CREATE_MOVIES_TABLE = '''
    CREATE TABLE IF NOT EXISTS MOVIES(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        RATING INTEGER NOT NULL
    )
'''

CREATE_PROJECTIONS_TABLE = '''
    CREATE TABLE IF NOT EXISTS PROJECTIONS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        MOVIE_ID INTEGER,
        TYPE TEXT NOT NULL,
        DATE TEXT NOT NULL,
        TIME TEXT NOT NULL,
        FOREIGN KEY (MOVIE_ID) REFERENCES MOVIES(ID)
    )
'''

CREATE_USERS_TABLE = '''
    CREATE TABLE IF NOT EXISTS Users (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USERNAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL
    )
'''

CREATE_RESERVATIONS_TABLE = '''
    CREATE TABLE IF NOT EXISTS RESERVATIONS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USER_ID INTEGER NOT NULL,
        PROJECTION_ID INTEGER NOT NULL,
        ROW INTEGER NOT NULL,
        COL INT NOT NULL,
        FOREIGN KEY (USER_ID) REFERENCES USERS(ID),
        FOREIGN KEY (PROJECTION_ID) REFERENCES PROJECTIONS(ID)
    )
'''

# check if tables already exist

DROP_MOVIES_TABLE = '''
    DROP TABLE IF EXISTS MOVIES
'''

DROP_PROJECTIONS_TABLE = '''
    DROP TABLE IF EXISTS PROJECTIONS
'''

DROP_USERS_TABLE = '''
    DROP TABLE IF EXISTS USERS
'''

DROP_RESERVATIONS_TABLE = '''
    DROP TABLE IF EXISTS RESERVATIONS
'''

# insert into tables

INSERT_INTO_USERS = '''
    INSERT INTO USERS(username, password) 
    VALUES(?,?)
'''

INSERT_INTO_MOVIES = '''
    INSERT INTO MOVIES(name, rating) 
    VALUES(?, ?)
'''

INSERT_INTO_PROJECTIONS = '''
    INSERT INTO PROJECTIONS(movie_id, type, date, time) 
    VALUES(?, ?, ?, ?)
'''

INSERT_INTO_RESERVATIONS = '''
    INSERT INTO RESERVATIONS(user_id, projection_id, row, col) 
    VALUES(?, ?, ?, ?)
'''

# show movies

MOVIES_ORDERED_BY_RATING = '''
    SELECT id, name, rating 
    FROM movies 
    ORDER BY rating
'''

# show projections

PROJECTIONS_1_ORDERED_BY_DATE = '''
    SELECT name, projections.id, date, time, type
    FROM projections
    JOIN movies
    ON projections.movie_id = movies.id
    WHERE movie_id = ?
'''

PROJECTIONS_2_ORDERED_BY_DATE = '''
    SELECT name, projections.id, date, time, type
    FROM projections
    JOIN movies
    ON projections.movie_id = movies.id
    WHERE movie_id = ? AND date = ?
'''

# validate user

SELECT_ALL_USERS = '''
    SELECT username
    FROM users
'''
# validate passwords

SELECT_ALL_PASSWORDS = '''
    SELECT password
    FROM users
'''

# available sits

SELECT_ALL_TAKEN_SITS ='''
    SELECT row, col
    FROM reservations
    WHERE projection_id = ?
'''

# check if sit is taken

RESERVE_SIT = '''
    INSERT INTO RESERVATIONS(user_id, projection_id, row, col) 
    VALUES(?, ?, ?, ?)
'''
# get user's id

GET_USER_ID = '''
    SELECT id
    FROM users
    WHERE username = ?
'''







