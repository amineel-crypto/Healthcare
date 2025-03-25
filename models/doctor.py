class Doctor:
    def __init__(self, name: str, specialization: str, contact: str):
        """
        Represents a doctor in the system.

        :param name: Name of the doctor (str)
        :param specialization: Specialization of the doctor (str)
        :param contact: Contact information of the doctor (str)
        """
        self.doctor_id = None  # Will be set when added to the database
        self.name = name
        self.specialization = specialization
        self.contact = contact

    def __str__(self):
        return f"Doctor(ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}, Contact: {self.contact})"