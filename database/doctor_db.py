import sqlite3
from sqlite3 import Error
from database.db_connection import get_db

def add_doctor(doctor):
    """
    Add a new doctor to the database.

    :param doctor: Doctor object to be added
    """
    conn = get_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Doctors (name, specialization, contact) VALUES (?, ?, ?)",
                (doctor.name, doctor.specialization, doctor.contact)
            )
            conn.commit()
            doctor.doctor_id = cursor.lastrowid  # Assign the auto-generated ID
        except Error as e:
            print(f"Error adding doctor: {e}")
        finally:
            conn.close()

def get_all_doctors():
    """
    Retrieve all doctors from the database.

    :return: List of tuples containing doctor data
    """
    conn = get_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Doctors")
            return cursor.fetchall()
        except Error as e:
            print(f"Error fetching doctors: {e}")
        finally:
            conn.close()
    return []

def doctor_exists(name, specialization, contact):
    """
    Check if a doctor with the same name, specialization, and contact already exists in the database.

    :param name: Name of the doctor (str)
    :param specialization: Specialization of the doctor (str)
    :param contact: Contact information of the doctor (str)
    :return: True if the doctor exists, False otherwise
    """
    conn = get_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM Doctors WHERE name = ? AND specialization = ? AND contact = ?",
                (name, specialization, contact)
            )
            return cursor.fetchone() is not None
        except Error as e:
            print(f"Error checking for doctor: {e}")
        finally:
            conn.close()
    return False

def delete_doctor(doctor_id):
    """
    Delete a doctor from the database.

    :param doctor_id: ID of the doctor to be deleted
    """
    conn = get_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Doctors WHERE doctor_id = ?", (doctor_id,))
            conn.commit()
        except Error as e:
            print(f"Error deleting doctor: {e}")
        finally:
            conn.close()

def update_doctor(doctor_id, name, specialization, contact):
    """
    Update a doctor's details in the database.

    :param doctor_id: ID of the doctor to be updated
    :param name: Updated name of the doctor (str)
    :param specialization: Updated specialization of the doctor (str)
    :param contact: Updated contact information of the doctor (str)
    """
    conn = get_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE Doctors SET name = ?, specialization = ?, contact = ? WHERE doctor_id = ?",
                (name, specialization, contact, doctor_id)
            )
            conn.commit()
        except Error as e:
            print(f"Error updating doctor: {e}")
        finally:
            conn.close()