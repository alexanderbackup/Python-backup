#import ipdb
import sqlite3
from ikea.base import BaseMeta
from ikea.custom_queries import *

           
class BaseModel(metaclass=BaseMeta):
   
    @classmethod
    def create_all_tables(cls):        
#        db = sqlite3.connect(DB_NAME)
#        c = db.cursor()

        for _table_name, _table_content in cls._tables.items():
            create_table(_table_name, _table_content)
#        db.commit()                
        
    @classmethod
    def create_obj(cls, **kwargs):
#        db = sqlite3.connect(DB_NAME)
#        c = db.cursor()    
        insert_into_table(cls.__name__, **kwargs)
#        db.commit()        

    @classmethod
    def filter(cls, **kwargs):
#        db = sqlite3.connect(DB_NAME)
#        c = db.cursor()      
        filter_table(cls.__name__, **kwargs)
        
#        db.commit()        
          
