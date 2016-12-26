import sqlite3
from sys import exit
from queries.manage_db_queries import *
from user_interface.validators import *
from user_interface.movie import show_movies
from user_interface.projection import show_projections
from user_interface.reservation import make_reservation
from user_interface.user import log_user


class CinemaInterface:
    
    def __init__(self):
        self.db = sqlite3.connect(DB_NAME)
        self.c = self.db.cursor()
  
    def _show_movies(self):
        show_movies(self.c)

    def _show_projections(self, answer):
        show_projections(self.c, answer)

    def _make_reservation(self):
        make_reservation(user, passowrd)
        
    @validate_password
    @hash_password
    def _log_user(self):
        return log_user()
            
        
#    @validate_password
#    @hash_password
#    def set_password(password):
#        pass


    @log_info
    def finalize(self):
        pass
        
    def _exit(self):
        return exit(0)
        
        
        
        
        
        
