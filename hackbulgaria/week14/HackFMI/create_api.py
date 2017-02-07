from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship


Base = declarative_base()


class MentorList(Base):

    __tablename__ = 'mentor'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(250))
    picture = Column(String(250))
    team_id = relationship('PublicTeam')

    
class PublicTeam(Base):

    __tablename__ = 'team'
    id = Column(Integer, primary_key=True)
    mentor_id = Column(Integer, ForeignKey('mentor.id'))
    name = Column(String(30))
    idea_description = Column(String(250))
    repository = Column(String(250))
    #technologies_full = relationship('SkillListApi')


class SkillListApi(Base):

    __tablename__ = 'skill'
    id = Column(Integer, primary_key=True)
    #team_id = Column(Integer, ForeignKey('team.id'))
    name = Column(String(250))
      

DB_NAME = 'Hackaton.db'

engine = create_engine('sqlite:///Hackaton.db')
Base.metadata.create_all(engine)


