import sqlite3
import os
from sqlite3 import Error

def get_db():
    try:
        conn = sqlite3.connect('healthcare.db')
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def initialize_db():
    conn = get_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            # Create Patients table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Patients (
                    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    contact TEXT NOT NULL,
                    medical_history TEXT
                )
            ''')
            
            # Create Doctors table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Doctors (
                    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    specialization TEXT NOT NULL,
                    cabinet_number INTEGER NOT NULL UNIQUE,
                    working_hours_start TIME NOT NULL DEFAULT '08:00',
                    working_hours_end TIME NOT NULL DEFAULT '15:00'
                )
            ''')
            
            # Create Appointments table with cabinet information
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Appointments (
                    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    patient_id INTEGER NOT NULL,
                    doctor_id INTEGER NOT NULL,
                    appointment_date DATETIME NOT NULL,
                    reason TEXT,
                    cabinet_number INTEGER NOT NULL,
                    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
                    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id),
                    FOREIGN KEY (cabinet_number) REFERENCES Doctors(cabinet_number),
                    UNIQUE (doctor_id, appointment_date),
                    UNIQUE (cabinet_number, appointment_date)
                )
            ''')
            
            # Create index for faster appointment lookups
            cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_appointment_date 
                ON Appointments(appointment_date)
            ''')
            
            conn.commit()
            print("Database initialized successfully")
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            conn.close()
    else:
        print("Failed to initialize database")