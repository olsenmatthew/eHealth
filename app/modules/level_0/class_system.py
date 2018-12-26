import pickle, random

class System: 

    # search the database for a user by their email or iserID, 
    # if found it returns the user object, otherwise it return false
    def get_user(email_or_userID):
        users_file = open("app/db/users", "rb")
        try:
            dict_users = pickle.load(users_file)
        except:
            return None
        for key in dict_users:
            if dict_users[key].email == email_or_userID or \
            key == email_or_userID:
                return dict_users[key]
        return None

    # search the database for a user by their email or iserID, 
    # if found it returns the user object, otherwise it return false
    def get_centre(abn_or_centreID):
        centres_file = open("app/db/centres", "rb")
        try:
            dict_centres = pickle.load(centres_file)
        except:
            return None
        for key in dict_centres:
            if dict_centres[key].abn == abn_or_centreID or \
            key == abn_or_centreID:
                return dict_centres[key]
        return None

    # search the database for a user by their email or iserID, 
    # if found it returns the user object, otherwise it return false
    def get_appointment(appID):
        apps_file = open("app/db/appointments", "rb")
        try:
            list_apps = pickle.load(apps_file)
        except:
            return None
        for app in list_apps:
            if app.appointmentID == appID:
                return app
        return None
    
    # search the database for a user by their email or iserID, 
    # if found it returns the user object, otherwise it return false
    def get_note(noteID):
        notes_file = open("app/db/notes", "rb")
        try:
            dict_notes = pickle.load(notes_file)
        except:
            return None
        for key in dict_notes:
            if key == noteID:
                return dict_notes[key]
        return None

    # generates a unique user identification number
    def generate_user_id():
        users_file = open("app/db/users", "rb")
        try:
            dict_users = pickle.load(users_file)
        except: 
            newID= str("usr-" + str(random.randint(1000, 100000)))
            return newID
        newID = str("usr-" + str(random.randint(1000, 1000000)))
        is_uniqueID = False
        while is_uniqueID is False:
            newID = str("usr-" + str(random.randint(1000, 1000000)))          
            for key in dict_users:
                if key is newID:
                    continue
            is_uniqueID = True
        return newID

    # generates a unique centre identification number        
    def generate_centre_id():
        centres_file = open("app/db/centres", "rb")
        try:
            dict_centres = pickle.load(centres_file)
        except: 
            newID= str("c-" + str(random.randint(1000, 100000)))
            return newID
        newID = str("c-" + str(random.randint(1000, 1000000)))
        is_uniqueID = False
        while is_uniqueID is False:
            newID = str("c-" + str(random.randint(1000, 1000000)))          
            for key in dict_centres:
                if key is newID:
                    continue
            is_uniqueID = True
        return newID

    # generates a unique appointment identification number
    def generate_appointment_id():
        appointments_file = open("app/db/appointments", "rb")
        try:
            list_appointments = pickle.load(appointments_file)
        except:
            newID= str("c-" + str(random.randint(1000, 100000)))
            return newID
        newID = str("c-" + str(random.randint(1000, 1000000)))
        is_uniqueID = False
        while is_uniqueID is False:
            newID = str("c-" + str(random.randint(1000, 1000000)))  
            for app in list_appointments:
                if app.appointmentID == newID:
                    continue
            is_uniqueID = True
        return newID

    # generates a unique note identification number
    def generate_note_id():
        notes_file = open("app/db/notes", "rb")
        try:
            dict_notes = pickle.load(notes_file)
        except: 
            newID= str("n-" + str(random.randint(1000, 100000)))
            return newID
        newID = str("n-" + str(random.randint(1000, 1000000)))
        is_uniqueID = False
        while is_uniqueID is False:
            newID = str("n-" + str(random.randint(1000, 1000000)))          
            for key in dict_notes:
                if key is newID:
                    continue
            is_uniqueID = True
        return newID

    # returns a dictionary of all registered users
    def get_users():
        users_file = open("app/db/users", "rb")
        try:
            dict_users = pickle.load(users_file)
        except:
            dict_users = {}
        users_file.close()
        return dict_users
    
    # returns a dictionary of all centres
    def get_centres():
        centres_file = open("app/db/centres", "rb")
        try:
            dict_centres = pickle.load(centres_file)
        except:
            dict_centres = {}
        centres_file.close()
        return dict_centres
   
    # returns a list of all provider/centre relationships
    def get_employment():
        employment_file = open("app/db/employment", "rb")
        try:
            list_employment = pickle.load(employment_file)
        except:
            list_employment = []
        employment_file.close()
        return list_employment

    # returns a list of all patient provider relationships
    def get_customers():
        customers_file = open("app/db/customers", "rb")
        try:
            list_customers = pickle.load(customers_file)
        except:
            list_customers = []
        customers_file.close()
        return list_customers

    # returns a dictionary of all appointments
    def get_appointments():
        app_file = open("app/db/appointments", "rb")
        try:
            list_appointments = pickle.load(app_file)
        except:
            list_appointments = [] 
        app_file.close()
        return list_appointments

    # returns a dictionary of all notes
    def get_notes():
        notes_file = open("app/db/notes", "rb")
        try:
            dict_notes = pickle.load(notes_file)
        except:
            dict_notes = {}
        notes_file.close()
        return dict_notes

    # returns a dictionary of all ratings
    def get_ratings():
        ratings_file = open("app/db/ratings", "rb")
        try: 
            list_ratings = pickle.load(ratings_file)
        except:
            list_ratings = []
        ratings_file.close()
        return list_ratings    

    # saves a dictionary of users to the users file, overwrites existing file
    def set_users(dict_users):
        users_file = open("app/db/users", "wb")
        pickle.dump(dict_users, users_file)
        users_file.close()

    # saves a dictionary of users to the centres file, overwrites existing file
    def set_centres(dict_centres):
        centres_file = open("app/db/centres", "wb")
        pickle.dump(dict_centres, centres_file)
        centres_file.close()

    # save a list of employment relationship to the employment file, overwrites existing file
    def set_employment(list_employment):
        employment_file = open("app/db/employment", "wb")
        pickle.dump(list_employment, employment_file)
        employment_file.close()

    # save a list of patient provider relationship to the customers file, overwrites existing file
    def set_customers(list_customers):
        customers_file = open("app/db/customers", "wb")
        pickle.dump(list_customers, customers_file)
        customers_file.close()
    
    # saves a dictionary of users to the appointments file, overwrites existing file
    def set_appointments(list_appointments):
        app_file = open("app/db/appointments", "wb")
        pickle.dump(list_appointments, app_file)
        app_file.close()

    # saves a dictionary of users to the notes file, overwrites existing filev
    def set_notes(dict_notes):
        note_file = open("app/db/notes", "wb")
        pickle.dump(dict_notes, note_file)
        note_file.close()

    # saves a dictionary of users to the provider ratings file, overwrites existing file
    def set_ratings(list_ratings):
        ratings_file = open("app/db/ratings", "wb")
        pickle.dump(list_ratings, ratings_file)
        ratings_file.close()