import sqlite3

# create data base

DB_NAME = "hospital2.db"
db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()

# create TABLES

drop_db = """DROP TABLE IF EXISTS PATIENT"""
c.execute(drop_db)
db.commit()

create_patients_table = """
CREATE TABLE IF NOT EXISTS PATIENT
(
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  FIRSTNAME VARCHAR(255) NOT NULL,
  LASTNAME VARCHAR(255) NOT NULL,
  AGE int NOT NULL,
  GENDER VARCHAR(6),
  DOCTOR INT,
  FOREIGN KEY(DOCTOR) REFERENCES DOCTORS(ID)
)
"""
c.execute(create_patients_table)
db.commit()

drop_db = """DROP TABLE IF EXISTS HOSPITAL_STAY"""
c.execute(drop_db)
db.commit()

create_patients_table = """
CREATE TABLE IF NOT EXISTS HOSPITAL_STAY
(
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  ROOM INT NOT NULL,
  STARTDATE DATE NOT NULL,
  ENDDATE DATE int,
  INJURY VARCHAR(255) NOT NULL,
  PATIENT INT,
  FOREIGN KEY(PATIENT) REFERENCES PATIENTS(ID)
)
"""
c.execute(create_patients_table)
db.commit()

drop_db = """DROP TABLE IF EXISTS DOCTORS"""
c.execute(drop_db)
db.commit()

create_patients_table = """
CREATE TABLE DOCTORS
(
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  FIRSTNAME VARCHAR(255) NOT NULL,
  LASTNAME VARCHAR(255) NOT NULL
)
"""
c.execute(create_patients_table)
db.commit()

# Populate PATIENT

insert_patient = """
INSERT INTO PATIENT (FIRSTNAME, LASTNAME, AGE)
VALUES(?, ?, ?)
"""
c.execute(insert_patient, (firstname, lastname, age))
db.commit()

# list all patients
list_patients = """SELECT * FROM PATIENT """
c.execute(list_patients)
print(c.fetchall())
db.commit()

