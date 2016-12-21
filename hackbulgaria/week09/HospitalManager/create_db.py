import sqlite3
from queries import *
from sys import exit
import hashlib
import getpass
import datetime
from settings import *
from random import choice


db = sqlite3.connect(DB_NAME)
c = db.cursor()

def create_tables():
    # Check if tables already exist
    c.execute(DROP_USER_TABLE)
    c.execute(DROP_PATIENT_TABLE)
    c.execute(DROP_DOCTOR_TABLE)
    c.execute(DROP_HOSPITAL_STAY_TABLE)
    c.execute(DROP_VISITATION_TABLE)
    db.commit()

    # Create new tables
    c.execute(CREATE_USER_TABLE)
    c.execute(CREATE_DOCTOR_TABLE)
    c.execute(CREATE_PATIENT_TABLE)
    c.execute(CREATE_HOSPITAL_STAY_TABLE)
    c.execute(CREATE_VISITATION_TABLE)
    db.commit()

def insert_users():
    users = [("Dr. Albena Bachvarova", "123456", 47),
             ("Kristina Valchanova", "123123", 20),
             ("Dr. Pavlina Zdravkova", "111111", 56),
             ("Pandio Pandev", "panda", 4),
             ("Slayana Monkova", "159357", 21),
             ("Kiril Ivanov", "kireto", 22),
             ("Dr. Georgi Georgiev", "doctora", 50)]
    c.executemany(INSERT_INTO_USER, users)
    db.commit()

def add_hospital_stay():
    patients = c.execute(SELECT_PATIENTS)

    for patient in patients:
        room = choice(ROOM_NUMBER)
        injury = choice(INJURy)
        startdate = str(datetime.datetime.now().date())
        enddate = str(datetime.datetime.now().date())
        c.execute(INSERT_INTO_HOSPITAL,
                  (room,
                   injury,
                   startdate,
                   enddate,
                   patient['ID']))
        
    db.commit()

class HospitalManager:

    def __init__(self):
        pass

    def log_into_system(self):
        pass

    def register_into_system(self):
        username = input('username:\n')
        is_doctor = False
        if 'Dr.' in username or 'dr.' in username:
            is_doctor = True
        password = self.hide_password()
        age = input('age:\n')
        if is_doctor:
            academic_title = input('academic title:\n')
            self.insert_user(username, 
                             password, 
                             age, 
                             [is_doctor, academic_title])
        else:
            print('choose a doctor to cure your diseases:\n')
            # tuple(id, username, academic_title)
            list_of_doctors = [i for i in 
                               c.execute(SELECT_DOCTORS_AND_DOC_ID)]
            for i in range(len(list_of_doctors)):
                print('{0}) {1}, {2}'.format(i+1, 
                                             list_of_doctors[i][1],
                                             list_of_doctors[i][2]))
            while True:
                answer = input()
                try:
                    chosen_doc = list_of_doctors[int(answer)-1][0]
                    break
                except:
                    print('Invalid input!')
            print('select a room from 1 to 10:')            
            while True:
                room = input()
                if room == '10' or (room in '123456789' 
                                    and len(room) < 2):
                    break
                print('Invalid input!')            
            print('what\'s your injury?')
            injury = input()
            print('choose how much you will stay(max of 9 days):')
            while True:
                staying = input()
                try:
                    staying = abs(int(staying))
                    if 0 == staying or staying > 9:
                        raise ValueError
                    break
                except:
                    print('Invalid input!')
                            
            self.insert_user(username,
                             password, 
                             age, 
                             [is_doctor, 
                              chosen_doc,
                              staying,
                              room, 
                              injury])
        print('success')                             
        # TODO: Auto Log in after registration !
#        auto_login(username, 
#                   password, 
#                   age, 
#                   [is_doctor, academic_title])

    def insert_user(self, username, password, age, is_doctor : list):
        if is_doctor[0]: # if is_doctor from register_into_system True
            c.execute(INSERT_USER_AS_DOCTOR, (username,
                                              password,
                                              age))
            take_last_id = c.lastrowid # shows last ID
            c.execute(INSERT_DOCTOR_VALUES, (take_last_id,
                                             is_doctor[1]))
            db.commit()
            return
        else: # it's a PATIENT !
            c.execute(INSERT_USER_AS_PATIENT, (username,
                                               password,
                                               age))
            take_last_id = c.lastrowid
            c.execute(INSERT_PATIENT_VALUES, (take_last_id,
                                              is_doctor[1]))
                                              
            # hospital stay is req for patients !
            startdate = datetime.date.today()
            enddate = startdate + datetime.timedelta(days=is_doctor[2])
            take_last_id = c.lastrowid
            c.execute(INSERT_PATIENT_IN_HOSPITAL, 
                                            (str(startdate),
                                             str(enddate),
                                             is_doctor[3],
                                             is_doctor[4],
                                             take_last_id))       
            db.commit()
            return

    def hide_password(self):

        def hash_pass(password):            
            hash_object = hashlib.sha512(password.encode())
            return hash_object.hexdigest()

        while True:
            password = getpass.getpass()
            validate_password = getpass.getpass()
            if password == validate_password:
                return hash_pass(password)
            print('Passwords do not match !\nTry again !')

    def help_main(self):
        pass

    def exit_system(self):
        return exit(0)


while True:
    print('''Welcome to Hospital Manager!\n
    Choose:\n
    1 to Log into the system,\n
    2 to register as a new user,\n
    3 for help main,\n
    4 to exit the system.\n''')
    foo = HospitalManager()
    answer = input()
    if answer == '1':
        pass
    elif answer == '2':
        foo.register_into_system()
    elif answer == '3':
        pass
    elif answer == '4':
        pass


