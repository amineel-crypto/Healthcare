import sqlite3
from database.db_connection import get_db

def add_patient(name, age, contact, medical_history):
    conn = get_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Patients (name, age, contact, medical_history)
                VALUES (?, ?, ?, ?)
            """, (name, age, contact, medical_history))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error adding patient: {e}")
            return False
        finally:
            conn.close()
    return False

def get_patients_by_name(name):
    conn = get_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM Patients 
                WHERE name LIKE ?
            """, (f"%{name}%",))
            patients = cursor.fetchall()
            return patients
        except sqlite3.Error as e:
            print(f"Error searching patients: {e}")
            return []
        finally:
            conn.close()
    return []

def get_all_patients():
    conn = get_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Patients")
            patients = cursor.fetchall()
            return patients
        except sqlite3.Error as e:
            print(f"Error getting patients: {e}")
            return []
        finally:
            conn.close()
    return [] 