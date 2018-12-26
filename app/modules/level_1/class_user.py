from flask_login import UserMixin
import statistics
from app.modules.level_0.class_system import *
from app.modules.level_0.class_rating import *
from app.modules.level_0.class_employment import *
from app.modules.level_0.class_customers import *

class User(UserMixin):

    def __init__(self, userID, name, surname, email, phone, password):
        self.userID = userID
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.email = email
        self.phone = phone
        self.password = password

    def get_id(self):
        return self.userID

    def set_name(self, name):
        self.name = name
    
    def set_surname(self, surname):
        self.surname = surname
    
    def set_email(self, email):
        self.email = email

    def set_phone(self, phone):
        self.phone = phone

    # Save the user object to the pickled users file, if the 
    # user already exists update the dictionary entry
    def set_user(self):
        system = System
        dict_users = system.get_users()
        if not dict_users: 
            dict_users = ({self.userID: self})
            system.set_users(dict_users)
            return 
        for key in dict_users:
            if key == self.userID:
                dict_users[key] = self
                system.set_users(dict_users)
                return
        dict_users.update({self.userID: self})
        system.set_users(dict_users)

    
    # If the user exists in the user file, delete it
    def delete_user(self):
        system = System
        dict_users = system.get_users()
        if dict_users is None:
            return None
        for key in dict_users:
            if dict_users[key].userID == self.userID:
                del dict_users[key]
                break
        system.set_users(dict_users)

class Patient(User):

    _type = "patient"

    def __init__(self, userID, name, surname, email, phone, password, medicareNo):
        super().__init__(userID, name, surname, email, phone, password)
        self.medicareNo = medicareNo

    def set_medicareNo(self, medicareNo):
        self.medicareNo = medicareNo

    # Provides a rating by the user for a provider or centre
    def rate(self, rating, entityID):
        system = System    # Set the system class
        list_ratings = system.get_ratings()   # get list of centre ratings from file
        have_rated = False               
        for r in list_ratings:
            if r.patientID == self.userID and r.entityID == entityID:
                r.rating = rating
                have_rated = True
                break
        if have_rated == False:
            new_rating = Rating(self.userID, entityID, rating)
            list_ratings.append(new_rating)
        system.set_ratings(list_ratings)      # Save new list of centre ratings to file
    
    # return the dictionary of appointments that a user is associated with
    def get_appointments(self):
        system = System
        my_appointments = []
        list_appointments = system.get_appointments()
        for app in list_appointments:
            if app.patient.userID == self.userID:
                my_appointments.append(app)
        return my_appointments

    def get_notes(self):
        system = System
        my_notes = []
        dict_notes = system.get_notes()
        for key in dict_notes:
            if self.userID == dict_notes[key].patient.userID:
                my_notes.append(dict_notes[key])
        return my_notes

    # Default print for patient object
    def __str__(self):
        return str("Patient: " + self.name + " " + self.surname + ", Email: " + str(self.userID))   

class Provider(User):

    _type = "provider"

    def __init__(self, userID, name, surname, email, phone, password, providerNo, profession):
        super().__init__(userID, name, surname, email, phone, password)
        self.providerNo = providerNo
        self.profession = profession.capitalize()

    def set_providerNo(self, providerNo):
        self.providerNo = providerNo
 
    def set_profession(self, profession):
        self.profession = profession

    # returns the providers rating
    def get_rating(self):
        system = System
        list_ratings = system.get_ratings()
        my_ratings = []
        if not list_ratings:
            return []
        for r in list_ratings:
            if r.entityID == self.userID:
                my_ratings.append(r.rating)
        if not my_ratings:
            return []
        return "{0:.2f}".format(statistics.mean(my_ratings))

    # returns a list of centres that the provider is associated with
    def get_centres(self):
        system = System
        dict_centres = system.get_centres()
        list_employment = system.get_employment()
        my_centres = []
        for emp in list_employment:
            if emp.provider.userID == self.userID:
                my_centres.append(dict_centres[emp.centre.centreID])
        return my_centres

    # returns a list of patients that the provider is associated with    
    def get_patients(self):
        system = System
        dict_users = system.get_users()
        list_customers = system.get_customers()
        my_patients = []
        for c in list_customers:
            if c.providerID == self.userID:
                my_patients.append(dict_users[c.patientID])
        return my_patients

    # returna list of appointments that a user is associated with
    def get_appointments(self):
        system = System
        my_appointments = []
        list_appointments = system.get_appointments()
        for app in list_appointments:
            if app.provider.userID == self.userID:
                app.patient = system.get_user(app.patient.userID)
                my_appointments.append(app)
        return my_appointments

    def __str__(self):
        return str("Provider: " + self.name + " " + self.surname + ", Email: " + str(self.userID))     

