import re
#import os
#import json
from collections import deque
import pickle


class Panda:
    
    def __init__(self, name, email, gender):
        self._name = name
        self._email = self.check_email(email)
        self._gender = gender
        #self.friends = []

    def name(self):
        return self._name

    def email(self):
        if not self._email:
            return False
        return self._email

    def gender(self):
        return self._gender

    def isMale(self):
        return bool(self._gender == 'male')

    def isFemale(self):
        return bool(self._gender == 'female')

    def __str__(self):
        return '{0} is {2} with email:{1}'.format(self._name,
                                                  self._email,
                                                  self._gender)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(str(self))

    def check_email(self, email):
        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            raise ValueError('Email is invalid')
        return email


class PandaSocialNetwork:
    
    def __init__(self):
        self.social_network = {}

    def get_pandas(self):
        return self.social_network.keys()

    def add_panda(self, panda):
        if panda in self.social_network:
            raise PandaAlreadyThere()
        self.social_network[panda] = set()
        

    def has_panda(self, panda):
        if panda in self.social_network:
            return True
        return False

    def make_friends(self, panda1, panda2):
        try:
            self.add_panda(panda1)
        except PandaAlreadyThere:
            pass
        try:
            self.add_panda(panda2)
        except PandaAlreadyThere:
            pass

        try:
            if not self.are_friends(panda1, panda2):
                self.social_network[panda1].add(panda2)
                self.social_network[panda2].add(panda1)
        except PandasAlreadyFriends:
            pass
  
    def are_friends(self, panda1, panda2):
        check1 = panda1 in self.social_network[panda2]
        check2 = panda2 in self.social_network[panda1]

        if (check1 and not check2) or (check2 and not check1):
            raise PandasAlreadyFriends()

        return check1 and check2

    def friends_of(self, panda):
        if panda in self.social_network:
            return [i for i in self.social_network[panda]]
        return False
    
    def connection_level(self, start: Panda, target: Panda):
        if not (self.has_panda(start) and self.has_panda(target)):
            return False
        q = deque()
        visited = set()
        paths = {start: None}

        q.append((0, start))
        visited.add(start)

        while q:
            level, current = q.popleft()

            if current == target:
                path = []

                while target is not None:
                    path.append(target)
                    target = paths[target]
                return level
                #return (level, reversed(path))

            for neigh in self.social_network[current]: # neighbour ! :D
                if neigh not in visited:
                    q.append((level+1, neigh))
                    visited.add(neigh)
                    paths[neigh] = current

        return -1

    def are_connected(self, panda1, panda2):
        if self.connection_level(panda1, panda2) == -1:
            return False
        return True

    def how_many_gender_in_network(self, level, panda, gender):
        count_match = 0
        q = deque()
        visited = set()
        paths = {panda: None}

        q.append((0, panda))
        visited.add(panda)

        while q:
            nivo, current = q.popleft()
            if nivo == level:
                return count_match

            for neigh in self.social_network[current]: # neighbour ! :D
                if neigh not in visited:
                    if neigh._gender == gender:
                        count_match += 1
                    q.append((nivo+1, neigh))
                    visited.add(neigh)
                    paths[neigh] = current
        return False # too many levels

    def save(self, file_name):
        fname = file_name +'.pkl'
        with open(fname, 'wb') as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def load(file_name):
        with open(file_name, 'rb') as f:
            new = pickle.load(f)
        return new

class PandaAlreadyThere(Exception):
    print('Panda already in network')

class PandasAlreadyFriends(Exception):
    print('Pandas already friends')


#    def save(self, file_name):
#        fname = file_name + '.json'
#        with open(fname, 'w') as f:
#            result = {}
#            for k,v in self.social_network.items():
#                smth = '{0},{1},{2}'.format(k._name, k._email, k._gender)
#                result[smth] = [(s._name, s._email, s._gender) for s in v]
#            json.dump(result, f, default=lambda o: o.__dict__, 
#            sort_keys=True, indent=4)
#    
#    @staticmethod
#    def load(file_name):
#        if not os.path.isfile(file_name):
#            print('No playlist with this name!')
#            return False
#        with open(file_name) as f:
#            load_ = json.load(f) # TODO: check for valid json!
#            assert isinstance(load_, dict)
#        new_psn = PandaSocialNetwork()
#        for k in load_:
#            temp = k.split(',') # ['Geri', '4@hackbulgaria.com', 'female'] from 'Geri,4@hackbulgaria.com,female'

#ivo = Panda("Ivo", "ivo@pandamai.lcom", "male")

#ivo.name() == "Ivo" # True
#ivo.email() == "ivo@pandamail.com"  # True
#ivo.gender() == "male" # True
#ivo.isMale() == True # True
#ivo.isFemale() == False # True
#panda1 = Panda('Ivo', '1@hackbulgaria.com', 'male')
#panda2 = Panda('Pe6o','2@hackbulgaria.com', 'male')
#panda3 = Panda('Lili', '3@hackbulgaria.com', 'female')
#panda4 = Panda('Geri', '4@hackbulgaria.com', 'female')
#foo = PandaSocialNetwork()
#foo.make_friends(panda1, panda2)
#foo.make_friends(panda2, panda3)
#foo.make_friends(panda3, panda4)
