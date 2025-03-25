class Patient:
    def __init__(self,name:str,age:int,contact:str,medical_history=""):
        self.patient_id=None #Wiil be set when added to the database
        self.name=name
        self.age=age
        self.contact=contact
        self.medical_history=medical_history