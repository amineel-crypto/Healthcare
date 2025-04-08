import customtkinter as ctk
from models.patient import Patient
from database.patient_db import *
import customtkinter as ctk
from PIL import Image
class PatientUI(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master,bg_color="#000")
        self.create_widgets()

    def create_widgets(self):
        # Configure rows and columns for layout
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)  # Expandable rows
        self.grid_columnconfigure(0, weight=1)         # Left-aligned widgets
        self.grid_columnconfigure(1, weight=0)         # Right-aligned background image

        # Header
        header_label = ctk.CTkLabel(
            self,
            text="Patient Management System",
            font=("Helvetica", 24, "bold"),
            text_color="#FFFFFF"  # White text for contrast
        )
        header_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        # Input Frame (to group labels and entries)
        input_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="#000")  # Dark theme
        input_frame.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        # Labels and Entry Widgets Inside the Input Frame
        label_width = 15  # Fixed width for labels to align them properly

        # Patient Name Label and Entry
        ctk.CTkLabel(input_frame, text="Patient Name:", anchor="w", width=label_width).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = ctk.CTkEntry(input_frame, width=200)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        # Age Label and Entry
        ctk.CTkLabel(input_frame, text="Age:", anchor="w", width=label_width).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.age_entry = ctk.CTkEntry(input_frame, width=200)
        self.age_entry.grid(row=1, column=1, padx=10, pady=5)

        # Contact Label and Entry
        ctk.CTkLabel(input_frame, text="Contact:", anchor="w", width=label_width).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.contact_entry = ctk.CTkEntry(input_frame, width=200)
        self.contact_entry.grid(row=2, column=1, padx=10, pady=5)

        # Medical History Label and Entry
        ctk.CTkLabel(input_frame, text="Medical History:", anchor="w", width=label_width).grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.medical_history_entry = ctk.CTkEntry(input_frame, width=200)
        self.medical_history_entry.grid(row=3, column=1, padx=10, pady=5)

        # Button Frame
        button_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="transparent")
        button_frame.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        add_button = ctk.CTkButton(button_frame, text="Add Patient", command=self.add_patient)
        add_button.pack(side="left", padx=10, pady=5)

        view_button = ctk.CTkButton(button_frame, text="View Patients", command=self.view_patients)
        view_button.pack(side="right", padx=10, pady=5)
        

        # Textbox Frame
        textbox_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="#333333")
        textbox_frame.grid(row=3, column=0, padx=20, pady=10, sticky="w")

        self.textbox = ctk.CTkTextbox(textbox_frame, width=500, height=200, corner_radius=10)
        self.textbox.pack(padx=10, pady=10)

        # Load and display the background image with rounded corners
        try:
            self.bg_image = Image.open("Abin Abraham Mammen.jpeg")  # Replace with your image file
            self.bg_image_tk = ctk.CTkImage(self.bg_image, size=(400, 600))  # Adjust size as needed

            # Create a frame with rounded corners for the background image
            bg_frame = ctk.CTkFrame(self, corner_radius=20, fg_color="transparent")
            bg_frame.place(relx=0.85, rely=0.5, anchor="center")

            bg_label = ctk.CTkLabel(bg_frame, image=self.bg_image_tk, text="")
            bg_label.pack(padx=5, pady=5)  # Padding ensures the rounded corners are visible
        except FileNotFoundError:
            print("Background image not found. Please check the file path.")

    def add_patient(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        contact = self.contact_entry.get()
        medical_history = self.medical_history_entry.get()

        patient = Patient(name, age, contact, medical_history)
        add_patient(patient)
        print("Patient added successfully!")

    def view_patients(self):
        self.textbox.delete("1.0", "end")
        patients = get_all_patients()
        for patient in patients:
            patient_info = (
                f"ID: {patient[0]}\n"
                f"Name: {patient[1]}\n"
                f"Age: {patient[2]}\n"
                f"Contact: {patient[3]}\n"
                f"Medical History: {patient[4]}\n"
                "-----------------------------------------------\n"
            )
            self.textbox.insert("end",patient_info)