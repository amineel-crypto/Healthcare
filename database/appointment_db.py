import sqlite3
from sqlite3 import Error
from database.db_connection import get_db
from models.appointment import Appointment

def add_appointment(appointment: Appointment) -> bool:
    """
    Add a new appointment to the database.
    
    Args:
        appointment: Appointment object to add
        
    Returns:
        bool: True if successful, False otherwise
    """
    conn = get_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO Appointments 
                (patient_id, doctor_id, appointment_date, reason) 
                VALUES (?, ?, ?, ?)""",
                (appointment.patient_id, appointment.doctor_id, 
                 appointment.appointment_date, appointment.reason)
            )
            conn.commit()
            appointment.appointment_id = cursor.lastrowid
            return True
        except Error as e:
            print(f"Error adding appointment: {e}")
            return False
        finally:
            conn.close()
    return False

def get_all_appointments() -> list:
    """
    Retrieve all appointments from the database.
    
    Returns:
        list: List of appointment tuples (id, patient_id, doctor_id, date, reason)
    """
    conn = get_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Appointments")
            return cursor.fetchall()
        except Error as e:
            print(f"Error fetching appointments: {e}")
            return []
        finally:
            conn.close()
    return []

def appointment_exists(patient_id: int, doctor_id: int, date: str,reason:str) -> bool:
    """
    Check if an appointment with the same patient, doctor and date exists.
    
    Args:
        patient_id: Patient ID
        doctor_id: Doctor ID
        date: Appointment date (YYYY-MM-DD)
        
    Returns:
        bool: True if exists, False otherwise
    """
    conn = get_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(
                """SELECT * FROM Appointments 
                WHERE patient_id = ? AND doctor_id = ? AND appointment_date = ? AND reason=?""",
                (patient_id, doctor_id, date,reason)
            )
            return cursor.fetchone() is not None
        except Error as e:
            print(f"Error checking appointment: {e}")
            return False
        finally:
            conn.close()
    return False

def delete_appointment(appointment_id: int) -> bool:
    """
    Delete an appointment by ID.
    
    Args:
        appointment_id: ID of appointment to delete
        
    Returns:
        bool: True if successful, False otherwise
    """
    conn = get_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM Appointments WHERE appointment_id = ?",
                (appointment_id,)
            )
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error deleting appointment: {e}")
            return False
        finally:
            conn.close()
    return False

def update_appointment(appointment_id: int, 
                      patient_id: int, 
                      doctor_id: int, 
                      date: str, 
                      reason: str) -> bool:
    """
    Update an existing appointment.
    
    Args:
        appointment_id: ID of appointment to update
        patient_id: New patient ID
        doctor_id: New doctor ID
        date: New appointment date
        reason: New reason
        
    Returns:
        bool: True if successful, False otherwise
    """
    conn = get_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE Appointments 
                SET patient_id = ?, doctor_id = ?, 
                    appointment_date = ?, reason = ?
                WHERE appointment_id = ?""",
                (patient_id, doctor_id, date, reason, appointment_id)
            )
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error updating appointment: {e}")
            return False
        finally:
            conn.close()
    return False

def get_appointments_by_patient(patient_id: int) -> list:
    """
    Get all appointments for a specific patient.
    
    Args:
        patient_id: ID of the patient
        
    Returns:
        list: List of appointment tuples
    """
    conn = get_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM Appointments WHERE patient_id = ?",
                (patient_id,)
            )
            return cursor.fetchall()
        except Error as e:
            print(f"Error fetching patient appointments: {e}")
            return []
        finally:
            conn.close()
    return []

def get_appointments_by_doctor(doctor_id: int) -> list:
    """
    Get all appointments for a specific doctor.
    
    Args:
        doctor_id: ID of the doctor
        
    Returns:
        list: List of appointment tuples
    """
    conn = get_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM Appointments WHERE doctor_id = ?",
                (doctor_id,)
            )
            return cursor.fetchall()
        except Error as e:
            print(f"Error fetching doctor appointments: {e}")
            return []
        finally:
            conn.close()
    return []