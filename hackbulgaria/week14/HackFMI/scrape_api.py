import requests


def get_mentor_list():
    
    mentor_list = requests.get('https://hackbulgaria.com/hackfmi/api/mentors/').json()
    return mentor_list
    
def get_public_team():

    public_team = requests.get('https://hackbulgaria.com/hackfmi/api/public-teams/').json()
    return public_team 
    
def get_skill_list_api():

    skill_list_api = requests.get('https://hackbulgaria.com/hackfmi/api/skills/').json()
    return skill_list_api 
