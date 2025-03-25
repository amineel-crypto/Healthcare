import customtkinter as ctk
from models.doctor import Doctor
from database.doctor_db import *
from tkinter import messagebox

class DoctorUI(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        # Labels
        ctk.CTkLabel(self, text="Doctor Name:").grid(row=0, column=0, padx=10, pady=10)
        ctk.CTkLabel(self, text="Specialization:").grid(row=1, column=0, padx=10, pady=10)
        ctk.CTkLabel(self, text="Contact:").grid(row=2, column=0, padx=10, pady=10)

        # Entry Widgets
        self.name_entry = ctk.CTkEntry(self)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.specialization_entry = ctk.CTkEntry(self)
        self.specialization_entry.grid(row=1, column=1, padx=10, pady=10)

        self.contact_entry = ctk.CTkEntry(self)
        self.contact_entry.grid(row=2, column=1, padx=10, pady=10)

        # Buttons
        ctk.CTkButton(self, text="Add Doctor", command=self.add_doctor).grid(row=3, column=0, padx=10, pady=10)
        ctk.CTkButton(self, text="View Doctors", command=self.view_doctors).grid(row=3, column=1, padx=10, pady=10)
        ctk.CTkButton(self, text="Delete Doctor", command=self.delete_doctor).grid(row=4, column=0, padx=10, pady=10)
        ctk.CTkButton(self, text="Update Doctor", command=self.update_doctor).grid(row=4, column=1, padx=10, pady=10)

        # Listbox to display doctors
        self.doctor_listbox = ctk.CTkTextbox(self, width=400, height=150)
        self.doctor_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def add_doctor(self):
        # Get input values
        name = self.name_entry.get()
        specialization = self.specialization_entry.get()
        contact = self.contact_entry.get()

        # Validate inputs
        if not name or not specialization or not contact:
            messagebox.showerror("Error", "Please fill in all required fields (Name, Specialization, Contact).")
            return

        # Check if the doctor already exists
        if doctor_exists(name, specialization, contact):
            messagebox.showerror("Error", "Doctor already exists in the medical cabinet.")
            return

        # Create and add doctor
        doctor = Doctor(name, specialization, contact)
        add_doctor(doctor)
        messagebox.showinfo("Success", "Doctor added successfully!")

        # Clear input fields
        self.name_entry.delete(0, ctk.END)
        self.specialization_entry.delete(0, ctk.END)
        self.contact_entry.delete(0, ctk.END)

        # Refresh the doctor list
        self.view_doctors()

    def view_doctors(self):
        # Clear the listbox
        self.doctor_listbox.delete(1.0, ctk.END)

        # Fetch and display doctors
        doctors = get_all_doctors()
        if doctors:
            for doctor in doctors:
                self.doctor_listbox.insert(
                    ctk.END,
                    f"ID: {doctor[0]}, Name: {doctor[1]}, Specialization: {doctor[2]}, Contact: {doctor[3]}\n"
                )
        else:
            self.doctor_listbox.insert(ctk.END, "No doctors found.")

    def delete_doctor(self):
        # Get the selected doctor's ID
        selected_text = self.doctor_listbox.get("sel.first", "sel.last")
        if not selected_text:
            messagebox.showerror("Error", "Please select a doctor to delete.")
            return

        # Extract the doctor ID from the selected text
        doctor_id = int(selected_text.split(",")[0].split(": ")[1])

        # Delete the doctor
        delete_doctor(doctor_id)
        messagebox.showinfo("Success", "Doctor deleted successfully!")

        # Refresh the doctor list
        self.view_doctors()

    def update_doctor(self):
        # Get the selected doctor's ID
        selected_text = self.doctor_listbox.get("sel.first", "sel.last")
        if not selected_text:
            messagebox.showerror("Error", "Please select a doctor to update.")
            return

        # Extract the doctor ID from the selected text
        doctor_id = int(selected_text.split(",")[0].split(": ")[1])

        # Get updated values
        name = self.name_entry.get()
        specialization = self.specialization_entry.get()
        contact = self.contact_entry.get()

        # Validate inputs
        if not name or not specialization or not contact:
            messagebox.showerror("Error", "Please fill in all required fields (Name, Specialization, Contact).")
            return

        # Update the doctor
        update_doctor(doctor_id, name, specialization, contact)
        messagebox.showinfo("Success", "Doctor updated successfully!")

        # Clear input fields
        self.name_entry.delete(0, ctk.END)
        self.specialization_entry.delete(0, ctk.END)
        self.contact_entry.delete(0, ctk.END)

        # Refresh the doctor list
        self.view_doctors()