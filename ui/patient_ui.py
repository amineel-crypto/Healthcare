import customtkinter as ctk
from models.patient import Patient
from database.patient_db import *

class PatientUI(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        # Labels
        ctk.CTkLabel(self, text="Patient Name:").grid(row=0, column=0, padx=10, pady=10)
        ctk.CTkLabel(self, text="Age:").grid(row=1, column=0, padx=10, pady=10)
        ctk.CTkLabel(self, text="Contact:").grid(row=2, column=0, padx=10, pady=10)
        ctk.CTkLabel(self, text="Medical History:").grid(row=3, column=0, padx=10, pady=10)

        # Entry Widgets
        self.name_entry = ctk.CTkEntry(self)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.age_entry = ctk.CTkEntry(self)
        self.age_entry.grid(row=1, column=1, padx=10, pady=10)

        self.contact_entry = ctk.CTkEntry(self)
        self.contact_entry.grid(row=2, column=1, padx=10, pady=10)

        self.medical_history_entry = ctk.CTkEntry(self)
        self.medical_history_entry.grid(row=3, column=1, padx=10, pady=10)

        # Buttons
        ctk.CTkButton(self, text="Add Patient", command=self.add_patient).grid(row=4, column=0, padx=10, pady=10)
        ctk.CTkButton(self, text="View Patients", command=self.view_patients).grid(row=4, column=1, padx=10, pady=10)

    def add_patient(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        contact = self.contact_entry.get()
        medical_history = self.medical_history_entry.get()

        patient = Patient(name, age, contact, medical_history)
        add_patient(patient)
        print("Patient added successfully!")

    def view_patients(self):
        patients = get_all_patients()
        for patient in patients:
            print(f"ID: {patient[0]}, Name: {patient[1]}, Age: {patient[2]}, Contact: {patient[3]}, Medical History: {patient[4]}")