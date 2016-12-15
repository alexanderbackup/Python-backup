import sqlite3
import prettytable # env_hospital

"""
from prettytable import from_db_cursor

connection = sqlite3.connect("mydb.db")
cursor = connection.cursor()
cursor.execute("SELECT field1, field2, field3 FROM my_table")
mytable = from_db_cursor(cursor)
"""

DB_NAME = "new_hospital.db"
db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()

def list_patients():
    list_patients = """SELECT * FROM PATIENTS """
    result = c.execute(list_patients)
    for patient in result.fetchall():
        print(patient['firstname'], patient['lastname'], patient['age'])

def list_doctors():
    list_doctors = """SELECT * FROM DOCTORS """
    result = c.execute(list_patients)
    for doctor in result.fetchall():
        print(doctor['firstname'], doctor['lastname'], doctor['id'])

def add_new_patient():

    # TODO: make validatation for wrong input !
    firstname = input("First name: ")
    lastname = input("Last name: ")
    age = input("Age: ")
    gender = input("Gender(M/F): ") 
    doctor_id = input("Doctor ID: ")
    add_new_patient = """
    INSERT INTO PATIENTS (FIRSTNAME, LASTNAME, AGE, GENDER, DOCTOR)
    VALUES (?, ?, ?, ?, ?)
    """
    c.execute(add_new_patient, (firstname, 
                               lastname, 
                               age, 
                               gender, 
                               doctor_id))
    db.commit()

def add_new_doctor():

    # TODO: make validatation for wrong input !
    doctor_id = str(input("Doctor ID: "))
    firstname = input("Doctor's First name: ")
    lastname = input("Doctor's Last name: ")
    add_new_doctor = """
    INSERT INTO DOCTORS (ID, FIRSTNAME, LASTNAME)
    VALUES (?, ?, ?)
    """
    c.execute(add_new_doctor, (doctor_id, firstname, lastname))
    db.commit()


def add_hospital_stay_of_a_patient():

    # TODO: make validatation for wrong input !
    hospital_id = input("Hospital id: ")
    room = input("Room number: ")
    startdate = input("Start date: ")
    enddate = input("Enddate: ") 
    injury = input("Injury: ")
    patient = input("Patient ID: ")
    add_hospital_stay_of_a_patient = """
    INSERT INTO HOSPITAL_STAY (ID, ROOM, STARTDATE, ENDDATE, INJURY, PATIENT)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    c.execute(add_hospital_stay_of_a_patient, (hospital_id, 
                                               room, 
                                               startdate, 
                                               enddate, 
                                               injury,
                                               patient))
    db.commit()


def update_info(_table): # DOCTORS / HOSPITAL_STAY / PATIENTS
    cursor = db.execute('select * from {0}'.format(_table))
    names = list(map(lambda x: x[0], cursor.description))
    changes = {i:'' for i in names}
    for i in changes:
        changes[i] = input('Give a value for {0}\'s {1} (Type the same if you don\'t want it changed!): '.format(_table, i))
    
    if _table == 'doctors':
        update_doctors_information = """
        UPDATE DOCTORS
        SET ID = ?, firstname = ?, lastname = ?
        WHERE ID = ?
        """
        c.execute(update_doctors_information,(changes['ID'],
                                              changes['FIRSTNAME'],
                                              changes['LASTNAME'],
                                              changes['ID']))
        db.commit()
        return

    if _table == 'hospital_stay':
        update_hospital_information = """
        UPDATE HOSPITAL_STAY
        SET ID = ?, ROOM = ?, STARTDATE = ?, ENDDATE = ?, INJURY = ?, PATIENT = ?
        WHERE ID = ?
        """
        c.execute(update_hospital_information,(changes['ID'],
                                              changes['ROOM'],
                                              changes['STARTDATE'],
                                              changes['ENDDATE'],
                                              changes['INJURY'],
                                              changes['PATIENT'],
                                              changes['ID']))
        db.commit()
        return

    if _table == 'patients':
        update_patients_information = """
        UPDATE PATIENTS
        SET ID = ?, FIRSTNAME = ?, LASTNAME = ?, AGE = ?, GENDER = ?, DOCTOR = ?
        WHERE ID = ?
        """
        c.execute(update_patients_information,(changes['ID'],
                                              changes['FIRSTNAME'],
                                              changes['LASTNAME'],
                                              changes['AGE'],
                                              changes['GENDER'],
                                              changes['DOCTOR'],
                                              changes['ID']))
        db.commit()
        return

def delete_info(_table): # DOCTORS / HOSPITAL_STAY / PATIENTS
    cursor = db.execute('select * from {0}'.format(_table))
    names = list(map(lambda x: x[0], cursor.description))
    changes = {i:'' for i in names}
    for i in changes:
        changes[i] = input('Give a value for {0}\'s {1} (Type the same if you don\'t want it changed!): '.format(_table, i))
    
    if _table == 'doctors':
        delete_from_doctors = """
        DELETE FROM DOCTORS 
        WHERE ID = ? AND FIRSTNAME = ? AND LASTNAME = ?
        """
        c.execute(delete_from_doctors,(changes['ID'],
                                       changes['FIRSTNAME'],
                                       changes['LASTNAME']))
        db.commit()
        return

    if _table == 'hospital_stay':
        delete_from_hospital = """
        DELETE FROM hospital_stay 
        WHERE ID = ? AND ROOM = ? AND INJURY = ? AND PATIENT = ?
        """
        c.execute(delete_from_hospital, (changes['ID'],
                                         changes['ROOM'],
                                         changes['INJURY'],
                                         changes['PATIENT']))
        db.commit()
        return

    if _table == 'patients':
        delete_from_patients = """
        DELETE FROM patients 
        WHERE ID = ? AND FIRSTNAME = ? AND LASTNAME = ? AND AGE = ?
        """
        c.execute(delete_from_patients,(changes['ID'],
                                        changes['FIRSTNAME'],
                                        changes['LASTNAME'],
                                        changes['AGE']))
        db.commit()
        return

























