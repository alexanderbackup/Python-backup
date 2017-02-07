from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from client import Client
from validators import hash_password, validate_password


Base = declarative_base()

engine = create_engine("sqlite:///test_money.db")
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    balance = Column(Integer)
    message = Column(String)


def create_clients_table():
    Base.metadata.create(engine)
    
def change_message(new_message, logged_user):
    update_sql = '''UPDATE clients SET message = ?
                    WHERE id = ?''' 
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)



