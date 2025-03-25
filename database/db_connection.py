import sqlite3
from sqlite3 import Error

def get_db():
    db_path = "medical_cabinet.db"
    conn = None
    
    try:
        conn = sqlite3.connect(db_path)
        print("Connection to Sqlite db successful")
    except Error as e:
        print(f"Error connecting to Sqlite Db: {e}")
    return conn

def initialize_db():
    conn = get_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            # Create Patients table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Patients (
                    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER,
                    contact TEXT,
                    medical_history TEXT
                )
            """)

            # Create Doctors table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Doctors (
                    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,  # Fixed typo: INTGER -> INTEGER
                    name TEXT NOT NULL,
                    specialization TEXT,
                    contact TEXT
                )
            """)

            # Create Appointments table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Appointments (
                    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    patient_id INTEGER,
                    doctor_id INTEGER,
                    appointment_date TEXT,
                    reason TEXT,
                    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
                    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
                )
            """)

            conn.commit()
            print("Database initialized successfully")
        except Error as e:
            print(f"Error initializing database: {e}")
        finally:
            conn.close()