class Appointment:
    def __init__(self, patient_id: int, doctor_id: int, appointment_date: str, reason: str = ""):
        """
        Represents an appointment in the system.

        :param patient_id: ID of the patient (int)
        :param doctor_id: ID of the doctor (int)
        :param appointment_date: Date of the appointment (str in YYYY-MM-DD format)
        :param reason: Reason for the appointment (str, optional)
        """
        self.appointment_id = None  # Will be set when added to database
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.reason = reason

    def __str__(self):
        return (f"Appointment(ID: {self.appointment_id}, Patient ID: {self.patient_id}, "
                f"Doctor ID: {self.doctor_id}, Date: {self.appointment_date}, Reason: {self.reason})")