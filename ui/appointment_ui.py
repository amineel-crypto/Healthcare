import customtkinter as ctk
from models.appointment import Appointment
from database.appointment_db import *
from tkinter import messagebox

class AppointmentUI(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        
    def create_widgets(self):
        # Labels
        ctk.CTkLabel(self, text="Patient Name:").grid(row=0, column=0, padx=10, pady=10)
        ctk.CTkLabel(self, text="Doctor Name:").grid(row=1, column=0, padx=10, pady=10)
        ctk.CTkLabel(self, text="Appointment Date:").grid(row=2, column=0, padx=10, pady=10)
        ctk.CTkLabel(self, text="Time:").grid(row=3, column=0, padx=10, pady=10)
        ctk.CTkLabel(self, text="Reason:").grid(row=4, column=0, padx=10, pady=10)
        
        # Entry Widgets
        self.patient_name_entry = ctk.CTkEntry(self)
        self.patient_name_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.doctor_name_entry = ctk.CTkEntry(self)
        self.doctor_name_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.date_entry = ctk.CTkEntry(self, placeholder_text="YYYY-MM-DD")
        self.date_entry.grid(row=2, column=1, padx=10, pady=10)
        
        self.time_entry = ctk.CTkEntry(self, placeholder_text="HH:MM")
        self.time_entry.grid(row=3, column=1, padx=10, pady=10)
        
        self.reason_entry = ctk.CTkEntry(self)
        self.reason_entry.grid(row=4, column=1, padx=10, pady=10)
        
        # Buttons
        ctk.CTkButton(self, text="Add Appointment", command=self.add_appointment).grid(row=5, column=0, padx=10, pady=10)
        ctk.CTkButton(self, text="View Appointments", command=self.view_appointments).grid(row=5, column=1, padx=10, pady=10)
        ctk.CTkButton(self, text="Delete Appointment", command=self.delete_appointment).grid(row=6, column=0, padx=10, pady=10)
        ctk.CTkButton(self, text="Find By Patient", command=self.find_by_patient).grid(row=6, column=1, padx=10, pady=10)
        
        # Textbox to display appointments
        self.appointment_textbox = ctk.CTkTextbox(self, width=500, height=200)
        self.appointment_textbox.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
        
    def clear_entries(self):
        """Clear all entry fields"""
        self.patient_name_entry.delete(0, ctk.END)
        self.doctor_name_entry.delete(0, ctk.END)
        self.date_entry.delete(0, ctk.END)
        self.time_entry.delete(0, ctk.END)
        self.reason_entry.delete(0, ctk.END)
        
    def add_appointment(self):
        try:
            patient_name = self.patient_name_entry.get().strip()
            doctor_name = self.doctor_name_entry.get().strip()
            date = self.date_entry.get().strip()
            time = self.time_entry.get().strip()
            reason = self.reason_entry.get().strip()
            
            if not all([patient_name, doctor_name, date, time, reason]):
                messagebox.showerror("Error", "All fields are required")
                return
                
            # Check if the appointment already exists
            if appointment_exists(patient_name, doctor_name, date, time):
                messagebox.showerror("Error", "This appointment slot is already booked")
                return 
            
            # Create and add appointment
            appointment = Appointment(patient_name, doctor_name, date, time, reason)
            if add_appointment(appointment):
                messagebox.showinfo("Success", "Appointment added successfully")
                self.clear_entries()
                self.view_appointments()
            else:
                messagebox.showerror("Error", "Failed to add appointment")
                
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            
    def view_appointments(self):
        self.appointment_textbox.delete("1.0", "end")
        appointments = get_all_appointments()
        
        if not appointments:
            self.appointment_textbox.insert("end", "No appointments found")
            return 
        
        for appt in appointments:
            self.appointment_textbox.insert(
                "end", 
                f"Patient: {appt[0]} | Doctor: {appt[1]} | Date: {appt[2]} | Time: {appt[3]} | Reason: {appt[4]}\n"
            )
    
    def delete_appointment(self):
        try:
            # Get selected text (if any)
            selected_text = self.appointment_textbox.get("sel.first", "sel.last")
            if not selected_text.strip():
                messagebox.showerror("Error", "Please select an appointment to delete")
                return
                
            # Extract appointment ID from selected text
            appointment_id = int(selected_text.split("|")[0].split(":")[1].strip())
            
            if delete_appointment(appointment_id):
                messagebox.showinfo("Success", "Appointment deleted successfully")
                self.view_appointments()
            else:
                messagebox.showerror("Error", "Failed to delete appointment")
                
        except Exception as e:
            messagebox.showerror("Error", f"Please select a valid appointment line\n{str(e)}")
    
    def find_by_patient(self):
        patient_name = self.patient_name_entry.get()
        if not patient_name:
            messagebox.showerror("Error", "Please enter a Patient Name")
            return
            
        try:
            self.appointment_textbox.delete("1.0", "end")
            appointments = get_appointments_by_patient(patient_name)
            
            if not appointments:
                self.appointment_textbox.insert("end", f"No appointments found for patient name: {patient_name}")
                return
                
            for appt in appointments:
                self.appointment_textbox.insert(
                    "end",
                    f"ID: {appt[0]} | Patient: {appt[1]} | Doctor: {appt[2]} | Date: {appt[3]} | Time: {appt[4]} | Reason: {appt[5]}\n"
                )
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")