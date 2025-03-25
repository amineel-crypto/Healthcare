from database.db_connection import *
from models.patient import Patient
from sqlite3 import Error

def add_patient(patient):
    conn = get_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Patients (name, age, contact, medical_history) VALUES (?, ?, ?, ?)",
                (patient.name, patient.age, patient.contact, patient.medical_history)
            )
            conn.commit()
            patient.patient_id = cursor.lastrowid  # Assign the auto-generated ID
            print("Patient added successfully!")
        except Error as e:
            print(f"Error adding patient: {e}")
        finally:
            conn.close()

def get_all_patients():
    conn = get_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Patients")
            return cursor.fetchall()
        except Error as e:
            print(f"Error fetching patients: {e}")
        finally:
            conn.close()