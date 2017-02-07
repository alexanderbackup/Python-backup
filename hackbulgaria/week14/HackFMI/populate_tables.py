from sqlalchemy.orm import sessionmaker
from scrape_api import get_skill_list_api
from create_api import *


session = sessionmaker(bind=engine)()

def populate_skills():
    skill_list = get_skill_list_api() # list with json
    
    session.bulk_insert_mappings(SkillListApi, skill_list)
    
    session.commit()
    
populate_skills()
