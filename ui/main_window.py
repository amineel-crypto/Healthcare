import customtkinter as ctk
from ui.patient_ui import PatientUI
from ui.doctor_ui import DoctorUI
from ui.appointment_ui import AppointmentUI
from PIL import Image


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Medical Management System")
        self.geometry("800x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        # Create a tab view for navigation
        self.tab_view = ctk.CTkTabview(self)
        self.tab_view.pack(fill="both", expand=True)

        # Add tabs for each component
        self.tab_view.add("Patients")

        # Create a frame for the background image in the Patients tab
        self.patients_bg_frame = ctk.CTkFrame(self.tab_view.tab("Patients"))
        self.patients_bg_frame.pack(fill="both", expand=True)

        # Load and set the background image
        try:
            self.bg_image = Image.open("Abin Abraham Mammen.jpeg")
            self.bg_image = self.bg_image.resize((800, 600), Image.Resampling.LANCZOS)
            self.bg_photo = ctk.CTkImage(self.bg_image, size=(800, 600))
            
            # Create label for the background image
            self.patients_bg_label = ctk.CTkLabel(self.patients_bg_frame, image=self.bg_photo, text="")
            self.patients_bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except FileNotFoundError:
            print("Background image not found. Please add a background.jpg file to your project directory.")

        # Initialize the UI for each component
        self.patient_ui = PatientUI(self.patients_bg_frame)
        self.patient_ui.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()