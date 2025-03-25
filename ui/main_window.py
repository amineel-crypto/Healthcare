import customtkinter as ctk
from ui.patient_ui import PatientUI
from ui.doctor_ui import DoctorUI
from ui.appointment_ui import AppointmentUI


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Medical Management System")
        self.geometry("800x600")

        # Create a tab view for navigation
        self.tab_view = ctk.CTkTabview(self)
        self.tab_view.pack(fill="both", expand=True)

        # Add tabs for each component
        self.tab_view.add("Patients")
        self.tab_view.add("Doctors")
        self.tab_view.add("Appointments")

        # Initialize the UI for each component
        self.patient_ui = PatientUI(self.tab_view.tab("Patients"))
        self.patient_ui.pack(fill="both", expand=True)

        self.doctor_ui = DoctorUI(self.tab_view.tab("Doctors"))
        self.doctor_ui.pack(fill="both", expand=True)
        
        self.appointment_ui=AppointmentUI(self.tab_view.tab("Appointments"))
        self.appointment_ui.pack(fill="both",expand=True)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()