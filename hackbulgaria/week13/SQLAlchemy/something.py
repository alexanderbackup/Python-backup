from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy import create_engine

#from settings import DB_NAME


Base = declarative_base()


class BaseUser(Base):

    __tablename__ = 'baseuser'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

    
class Student(BaseUser):

    __tablename__ = 'student'
    id = Column(Integer, ForeignKey('baseuser.id'), primary_key=True)
    mac = Column(String(30))
    #course = Column(Integer, ForeignKey('course.id'))
    

DB_NAME = 'Odin.db'

engine = create_engine('sqlite:///Odin.db')
Base.metadata.create_all_tables()    
