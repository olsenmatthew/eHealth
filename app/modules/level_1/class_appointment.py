import statistics
from app.modules.level_0.class_system import *
from app.modules.level_0.class_customers import *

class Appointment():

    def __init__(self, appointmentID, patient, provider, centre, date_time, epoch_time):
        self.appointmentID = appointmentID
        self.patient = patient
        self.provider = provider
        self.centre = centre
        self.date_time = date_time
        self.epoch_time = epoch_time

    def set_appointment(self):
        system = System
        list_appointments = system.get_appointments()
        list_customers = system.get_customers()
        is_customer = False

        for c in list_customers:
            if c.providerID == self.provider.userID and c.patientID == self.patient.userID:
                is_customer = True
        if is_customer == False:
            customer = Customer(self.patient.userID, self.provider.userID)
            list_customers.append(customer)
        system.set_customers(list_customers)

        is_booked = False
        for app in list_appointments:
            if app.provider.userID == self.provider.userID and app.date_time == self.date_time:
                return "Not Available"
        list_appointments.append(self)
        system.set_appointments(list_appointments)
        return "Booking Success"
    
    def delete_appointment(self):
        system = System
        list_appointments = system.get_appointments()

        for app in list_appointments:
            if app.appointmentID == self.appointmentID:
                list_appointments.remove(app)
                break
        
        system.set_appointments(list_appointments)

    def __lt__(self, other):
        return self.epoch_time > other.epoch_time