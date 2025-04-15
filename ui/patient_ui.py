import customtkinter as ctk
from models.patient import Patient
from database.patient_db import *
import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
from datetime import datetime

class PatientUI(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master,bg_color="#000")
        self.create_widgets()

    def create_widgets(self):
        # Configure rows and columns for layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)  # Navbar column
        self.grid_columnconfigure(1, weight=1)  # Content column
        self.grid_columnconfigure(2, weight=0)  # Image column

        # Create navigation frame (sidebar)
        nav_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#1a1a1a", width=200)
        nav_frame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)

        # Navigation header
        nav_header = ctk.CTkLabel(
            nav_frame,
            text="Menu",
            font=("Helvetica", 20, "bold"),
            text_color="#FFFFFF"
        )
        nav_header.pack(pady=20)

        # Navigation buttons
        nav_buttons = [
            ("👤 Patient Info", self.show_patient_section),
            ("📅 Appointments", self.show_appointment_section),
            ("🔍 Search", self.show_search_section)
        ]

        for text, command in nav_buttons:
            btn = ctk.CTkButton(
                nav_frame,
                text=text,
                command=command,
                fg_color="transparent",
                hover_color="#2c2c2c",
                font=("Helvetica", 14),
                height=40,
                corner_radius=0,
                anchor="w"
            )
            btn.pack(fill="x", padx=10, pady=5)

        # Main content frame
        self.content_frame = ctk.CTkFrame(self, fg_color="#000")
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Image Frame (Right Side)
        image_frame = ctk.CTkFrame(self, corner_radius=20, fg_color="transparent")
        image_frame.grid(row=0, column=2, sticky="nsew", padx=20, pady=20)
        
        try:
            self.bg_image = Image.open("Abin Abraham Mammen.jpeg")
            self.bg_image_tk = ctk.CTkImage(self.bg_image, size=(400, 600))
            bg_label = ctk.CTkLabel(image_frame, image=self.bg_image_tk, text="")
            bg_label.pack(padx=5, pady=5)
        except FileNotFoundError:
            print("Background image not found. Please check the file path.")

        # Create sections
        self.create_patient_section()
        self.create_appointment_section()
        self.create_search_section()

        # Show initial section
        self.show_patient_section()

    def show_patient_section(self):
        self.patient_section.pack(fill="both", expand=True)
        self.appointment_section.pack_forget()
        self.search_section.pack_forget()

    def show_appointment_section(self):
        self.patient_section.pack_forget()
        self.appointment_section.pack(fill="both", expand=True)
        self.search_section.pack_forget()

    def show_search_section(self):
        self.patient_section.pack_forget()
        self.appointment_section.pack_forget()
        self.search_section.pack(fill="both", expand=True)

    def create_patient_section(self):
        self.patient_section = ctk.CTkScrollableFrame(self.content_frame, fg_color="#000")
        
        # Header
        header_frame = ctk.CTkFrame(self.patient_section, fg_color="transparent")
        header_frame.pack(fill="x", pady=(0, 20))
        
        header_label = ctk.CTkLabel(
            header_frame,
            text="Patient Information",
            font=("Helvetica", 28, "bold"),
            text_color="#FFFFFF"
        )
        header_label.pack(side="left")

        # Patient Information Form
        form_frame = ctk.CTkFrame(self.patient_section, corner_radius=15, fg_color="#1a1a1a", border_width=2, border_color="#2ecc71")
        form_frame.pack(fill="x", pady=10, padx=20)

        # Form Title
        form_title = ctk.CTkLabel(
            form_frame,
            text="New Patient Registration",
            font=("Helvetica", 18, "bold"),
            text_color="#2ecc71"
        )
        form_title.pack(pady=10)

        # Input Fields
        input_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        input_frame.pack(fill="x", padx=20, pady=10)

        # Patient Name
        name_frame = ctk.CTkFrame(input_frame, fg_color="transparent")
        name_frame.pack(fill="x", pady=8)
        ctk.CTkLabel(name_frame, text="👤 Patient Name:", width=20, font=("Helvetica", 14)).pack(side="left", padx=5)
        self.name_entry = ctk.CTkEntry(name_frame, width=300, font=("Helvetica", 14), corner_radius=8)
        self.name_entry.pack(side="left", padx=5, fill="x", expand=True)

        # Age
        age_frame = ctk.CTkFrame(input_frame, fg_color="transparent")
        age_frame.pack(fill="x", pady=8)
        ctk.CTkLabel(age_frame, text="📅 Age:", width=20, font=("Helvetica", 14)).pack(side="left", padx=5)
        self.age_entry = ctk.CTkEntry(age_frame, width=300, font=("Helvetica", 14), corner_radius=8)
        self.age_entry.pack(side="left", padx=5, fill="x", expand=True)

        # Contact
        contact_frame = ctk.CTkFrame(input_frame, fg_color="transparent")
        contact_frame.pack(fill="x", pady=8)
        ctk.CTkLabel(contact_frame, text="📞 Contact:", width=20, font=("Helvetica", 14)).pack(side="left", padx=5)
        self.contact_entry = ctk.CTkEntry(contact_frame, width=300, font=("Helvetica", 14), corner_radius=8)
        self.contact_entry.pack(side="left", padx=5, fill="x", expand=True)

        # Medical History
        history_frame = ctk.CTkFrame(input_frame, fg_color="transparent")
        history_frame.pack(fill="x", pady=8)
        ctk.CTkLabel(history_frame, text="🏥 Medical History:", width=20, font=("Helvetica", 14)).pack(side="left", padx=5)
        self.malady_var = ctk.StringVar(value="Select Condition")
        self.malady_options = ["Fever", "Cold", "Headache", "Other"]
        self.malady_dropdown = ctk.CTkOptionMenu(
            history_frame,
            values=self.malady_options,
            variable=self.malady_var,
            width=300,
            font=("Helvetica", 14),
            corner_radius=8,
            dropdown_font=("Helvetica", 14)
        )
        self.malady_dropdown.pack(side="left", padx=5, fill="x", expand=True)

        # Other Condition Entry
        self.other_malady_entry = ctk.CTkEntry(
            history_frame,
            width=300,
            placeholder_text="Specify other condition",
            font=("Helvetica", 14),
            corner_radius=8
        )
        self.other_malady_entry.pack(side="left", padx=5, fill="x", expand=True)
        self.other_malady_entry.pack_forget()

        # Buttons
        button_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        button_frame.pack(fill="x", padx=20, pady=15)

        add_button = ctk.CTkButton(
            button_frame,
            text="➕ Add Patient",
            command=self.add_patient,
            fg_color="#2ecc71",
            hover_color="#27ae60",
            font=("Helvetica", 14, "bold"),
            corner_radius=8,
            height=40
        )
        add_button.pack(side="left", padx=10)

        search_button = ctk.CTkButton(
            button_frame,
            text="🔍 Search Patient",
            command=self.search_by_name,
            fg_color="#3498db",
            hover_color="#2980b9",
            font=("Helvetica", 14, "bold"),
            corner_radius=8,
            height=40
        )
        search_button.pack(side="left", padx=10)

    def create_appointment_section(self):
        self.appointment_section = ctk.CTkScrollableFrame(self.content_frame, fg_color="#000")
        
        # Header
        header_frame = ctk.CTkFrame(self.appointment_section, fg_color="transparent")
        header_frame.pack(fill="x", pady=(0, 20))
        
        header_label = ctk.CTkLabel(
            header_frame,
            text="Appointment Scheduling",
            font=("Helvetica", 28, "bold"),
            text_color="#FFFFFF"
        )
        header_label.pack(side="left")

        # Appointment Form
        form_frame = ctk.CTkFrame(self.appointment_section, corner_radius=15, fg_color="#1a1a1a", border_width=2, border_color="#e74c3c")
        form_frame.pack(fill="x", pady=10, padx=20)

        # Form Title
        form_title = ctk.CTkLabel(
            form_frame,
            text="Schedule New Appointment",
            font=("Helvetica", 18, "bold"),
            text_color="#e74c3c"
        )
        form_title.pack(pady=10)

        # Input Fields
        input_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        input_frame.pack(fill="x", padx=20, pady=10)

        # Doctor Selection
        doctor_frame = ctk.CTkFrame(input_frame, fg_color="transparent")
        doctor_frame.pack(fill="x", pady=8)
        ctk.CTkLabel(doctor_frame, text="👨‍⚕️ Doctor:", width=20, font=("Helvetica", 14)).pack(side="left", padx=5)
        self.doctor_var = ctk.StringVar()
        self.doctor_dropdown = ctk.CTkOptionMenu(
            doctor_frame,
            variable=self.doctor_var,
            width=300,
            font=("Helvetica", 14),
            corner_radius=8,
            dropdown_font=("Helvetica", 14)
        )
        self.doctor_dropdown.pack(side="left", padx=5, fill="x", expand=True)

        # Date Selection
        date_frame = ctk.CTkFrame(input_frame, fg_color="transparent")
        date_frame.pack(fill="x", pady=8)
        ctk.CTkLabel(date_frame, text="📅 Date:", width=20, font=("Helvetica", 14)).pack(side="left", padx=5)
        self.date_entry = ctk.CTkEntry(
            date_frame,
            width=300,
            placeholder_text="YYYY-MM-DD",
            font=("Helvetica", 14),
            corner_radius=8
        )
        self.date_entry.pack(side="left", padx=5, fill="x", expand=True)

        # Time Selection
        time_frame = ctk.CTkFrame(input_frame, fg_color="transparent")
        time_frame.pack(fill="x", pady=8)
        ctk.CTkLabel(time_frame, text="⏰ Time:", width=20, font=("Helvetica", 14)).pack(side="left", padx=5)
        self.time_entry = ctk.CTkEntry(
            time_frame,
            width=300,
            placeholder_text="HH:MM",
            font=("Helvetica", 14),
            corner_radius=8
        )
        self.time_entry.pack(side="left", padx=5, fill="x", expand=True)

        # Reason
        reason_frame = ctk.CTkFrame(input_frame, fg_color="transparent")
        reason_frame.pack(fill="x", pady=8)
        ctk.CTkLabel(reason_frame, text="📝 Reason:", width=20, font=("Helvetica", 14)).pack(side="left", padx=5)
        self.reason_entry = ctk.CTkEntry(
            reason_frame,
            width=300,
            font=("Helvetica", 14),
            corner_radius=8
        )
        self.reason_entry.pack(side="left", padx=5, fill="x", expand=True)

        # Buttons
        button_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        button_frame.pack(fill="x", padx=20, pady=15)

        schedule_button = ctk.CTkButton(
            button_frame,
            text="📅 Schedule Appointment",
            command=self.schedule_appointment,
            fg_color="#e74c3c",
            hover_color="#c0392b",
            font=("Helvetica", 14, "bold"),
            corner_radius=8,
            height=40
        )
        schedule_button.pack(side="left", padx=10)

        view_appointments_button = ctk.CTkButton(
            button_frame,
            text="👁️ View Appointments",
            command=self.view_appointments,
            fg_color="#9b59b6",
            hover_color="#8e44ad",
            font=("Helvetica", 14, "bold"),
            corner_radius=8,
            height=40
        )
        view_appointments_button.pack(side="left", padx=10)

    def create_search_section(self):
        self.search_section = ctk.CTkScrollableFrame(self.content_frame, fg_color="#000")
        
        # Header
        header_frame = ctk.CTkFrame(self.search_section, fg_color="transparent")
        header_frame.pack(fill="x", pady=(0, 20))
        
        header_label = ctk.CTkLabel(
            header_frame,
            text="Search & Results",
            font=("Helvetica", 28, "bold"),
            text_color="#FFFFFF"
        )
        header_label.pack(side="left")

        # Search Form
        form_frame = ctk.CTkFrame(self.search_section, corner_radius=15, fg_color="#1a1a1a", border_width=2, border_color="#3498db")
        form_frame.pack(fill="x", pady=10, padx=20)

        # Form Title
        form_title = ctk.CTkLabel(
            form_frame,
            text="Search Patients",
            font=("Helvetica", 18, "bold"),
            text_color="#3498db"
        )
        form_title.pack(pady=10)

        # Search Input
        search_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        search_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(search_frame, text="🔍 Search by Name:", width=20, font=("Helvetica", 14)).pack(side="left", padx=5)
        self.search_entry = ctk.CTkEntry(
            search_frame,
            width=300,
            font=("Helvetica", 14),
            corner_radius=8
        )
        self.search_entry.pack(side="left", padx=5, fill="x", expand=True)

        search_button = ctk.CTkButton(
            search_frame,
            text="Search",
            command=self.search_by_name,
            fg_color="#3498db",
            hover_color="#2980b9",
            font=("Helvetica", 14, "bold"),
            corner_radius=8,
            height=40
        )
        search_button.pack(side="left", padx=10)

        # Results Section
        results_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        results_frame.pack(fill="x", padx=20, pady=10)

        self.result_textbox = ctk.CTkTextbox(
            results_frame,
            width=600,
            height=200,
            corner_radius=10,
            fg_color="#2c2c2c",
            text_color="#FFFFFF",
            font=("Helvetica", 14),
            scrollbar_button_color="#3498db",
            scrollbar_button_hover_color="#2980b9"
        )
        self.result_textbox.pack(fill="x", pady=10)

    def load_doctors(self):
        conn = get_db()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT doctor_id, name, specialization FROM Doctors")
                doctors = cursor.fetchall()
                doctor_options = [f"{d[0]} - {d[1]} ({d[2]})" for d in doctors]
                self.doctor_dropdown.configure(values=doctor_options)
                if doctor_options:
                    self.doctor_var.set(doctor_options[0])
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load doctors: {str(e)}")
            finally:
                conn.close()

    def on_malady_select(self, choice):
        if choice == "Other":
            self.other_malady_entry.pack()
        else:
            self.other_malady_entry.pack_forget()

    def add_patient(self):
        # Get all input values
        name = self.name_entry.get().strip()
        age_text = self.age_entry.get().strip()
        contact = self.contact_entry.get().strip()
        malady = self.malady_var.get()
        
        # If "Other" is selected, get the custom malady
        if malady == "Other":
            malady = self.other_malady_entry.get().strip()
            if not malady:
                messagebox.showerror("Error", "Please specify the other malady")
                return

        # Check if any required field is empty
        if not name or not age_text or not contact or malady == "Select Condition":
            messagebox.showerror("Error", "Please fill in all required fields (Name, Age, Contact, Malady)")
            return

        try:
            # Convert age to integer
            age = int(age_text)
            
            # Create and add patient
            patient = Patient(name, age, contact, malady)
            patient_id = add_patient(patient)
            
            # Show success message with patient ID
            messagebox.showinfo("Success", f"Patient added successfully!\nPatient ID: {patient_id}")
            
            # Clear the entries
            self.name_entry.delete(0, ctk.END)
            self.age_entry.delete(0, ctk.END)
            self.contact_entry.delete(0, ctk.END)
            self.malady_var.set("Select Condition")
            self.other_malady_entry.delete(0, ctk.END)
            self.other_malady_entry.pack_forget()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid age (number)")

    def search_by_name(self):
        # Clear previous results
        self.result_textbox.delete("1.0", "end")
        
        # Get the search name from the search entry field
        search_name = self.search_entry.get().strip()
        
        if not search_name:
            messagebox.showerror("Error", "Please enter a patient name to search")
            return
            
        try:
            conn = get_db()
            if conn is not None:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT patient_id, name, age, contact, medical_history 
                    FROM Patients 
                    WHERE name LIKE ?
                """, (f"%{search_name}%",))
                
                patients = cursor.fetchall()
                
                if patients:
                    self.result_textbox.insert("end", f"Search Results for '{search_name}':\n\n")
                    for patient in patients:
                        patient_info = (
                            f"Patient ID: {patient[0]}\n"
                            f"Name: {patient[1]}\n"
                            f"Age: {patient[2]}\n"
                            f"Contact: {patient[3]}\n"
                            f"Medical History: {patient[4]}\n"
                            "-----------------------------------------------\n"
                        )
                        self.result_textbox.insert("end", patient_info)
                else:
                    self.result_textbox.insert("end", f"No patients found with name containing: {search_name}")
                
                conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to search patients: {str(e)}")
            self.result_textbox.insert("end", "An error occurred while searching for patients.")

    def schedule_appointment(self):
        # Get selected patient and doctor IDs
        patient_name = self.name_entry.get().strip()
        if not patient_name:
            messagebox.showerror("Error", "Please enter a patient name first")
            return

        doctor_id = self.doctor_var.get().split(" - ")[0]
        
        # Get date and time
        date = self.date_entry.get()
        time = self.time_entry.get()
        reason = self.reason_entry.get()

        # Validate inputs
        if not all([patient_name, doctor_id, date, time, reason]):
            messagebox.showerror("Error", "Please fill in all appointment fields")
            return

        try:
            # Parse and validate time
            appointment_time = datetime.strptime(time, "%H:%M").time()
            if appointment_time < datetime.strptime("08:00", "%H:%M").time() or \
               appointment_time > datetime.strptime("15:00", "%H:%M").time():
                messagebox.showerror("Error", "Appointments are only available between 8:00 and 15:00")
                return

            # Combine date and time
            appointment_datetime = f"{date} {time}"
            datetime.strptime(appointment_datetime, "%Y-%m-%d %H:%M")
        except ValueError:
            messagebox.showerror("Error", "Invalid date or time format. Use YYYY-MM-DD and HH:MM")
            return

        # Check for appointment conflicts
        conn = get_db()
        if conn is not None:
            try:
                cursor = conn.cursor()
                
                # Get patient ID
                cursor.execute("SELECT patient_id FROM Patients WHERE name = ?", (patient_name,))
                patient = cursor.fetchone()
                if not patient:
                    messagebox.showerror("Error", "Patient not found. Please add the patient first.")
                    return

                patient_id = patient[0]
                
                # Check for existing appointments at the same time
                cursor.execute("""
                    SELECT COUNT(*) FROM Appointments 
                    WHERE appointment_date = ? AND doctor_id = ?
                """, (appointment_datetime, doctor_id))
                
                if cursor.fetchone()[0] > 0:
                    messagebox.showerror("Error", "This time slot is already booked. Please choose another time.")
                    return
                
                # Check for patient's existing appointments on the same day
                cursor.execute("""
                    SELECT COUNT(*) FROM Appointments 
                    WHERE patient_id = ? AND DATE(appointment_date) = DATE(?)
                """, (patient_id, appointment_datetime))
                
                if cursor.fetchone()[0] > 0:
                    messagebox.showerror("Error", "Patient already has an appointment on this day.")
                    return
                
                # Insert appointment
                cursor.execute("""
                    INSERT INTO Appointments (patient_id, doctor_id, appointment_date, reason)
                    VALUES (?, ?, ?, ?)
                """, (patient_id, doctor_id, appointment_datetime, reason))
                conn.commit()
                messagebox.showinfo("Success", "Appointment scheduled successfully!")
                self.clear_appointment_form()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to schedule appointment: {str(e)}")
            finally:
                conn.close()

    def clear_appointment_form(self):
        self.date_entry.delete(0, "end")
        self.time_entry.delete(0, "end")
        self.reason_entry.delete(0, "end")

    def view_appointments(self):
        # Clear previous results
        self.result_textbox.delete("1.0", "end")
        
        # Get the patient name
        patient_name = self.name_entry.get().strip()
        if not patient_name:
            messagebox.showerror("Error", "Please enter a patient name first")
            return

        try:
            conn = get_db()
            if conn is not None:
                cursor = conn.cursor()
                
                # Get patient's appointments
                cursor.execute("""
                    SELECT 
                        a.appointment_id,
                        a.appointment_date,
                        d.name as doctor_name,
                        d.specialization,
                        d.cabinet_number,
                        a.reason
                    FROM Appointments a
                    JOIN Doctors d ON a.doctor_id = d.doctor_id
                    JOIN Patients p ON a.patient_id = p.patient_id
                    WHERE p.name = ?
                    ORDER BY a.appointment_date
                """, (patient_name,))
                
                appointments = cursor.fetchall()
                
                if appointments:
                    self.result_textbox.insert("end", f"Appointments for {patient_name}:\n\n")
                    for appt in appointments:
                        appointment_info = (
                            f"Appointment ID: {appt[0]}\n"
                            f"Date & Time: {appt[1]}\n"
                            f"Doctor: {appt[2]} ({appt[3]})\n"
                            f"Cabinet: {appt[4]}\n"
                            f"Reason: {appt[5]}\n"
                            "-----------------------------------------------\n"
                        )
                        self.result_textbox.insert("end", appointment_info)
                else:
                    self.result_textbox.insert("end", f"No appointments found for {patient_name}")
                
                conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to view appointments: {str(e)}")
            self.result_textbox.insert("end", "An error occurred while fetching appointments.")