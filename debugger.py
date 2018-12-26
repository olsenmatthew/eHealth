from app.modules.level_0.class_system import *
from app.modules.level_1.class_user import *
from app.modules.level_1.class_centre import *
from app.modules.level_1.class_appointment import *
from app.modules.level_0.class_rating import *

system = System

# if system.get_user("s@gmail.com") == False:
#     patient1 = Patient(system.generate_user_id(), "sam", "gibbs", "s@gmail.com", '04023', "password", '111')
#     patient1.set_user()
# if system.get_user("h@gmail.com") == False:
#     patient2 = Patient(system.generate_user_id(), "Harold", "Newman", "h@gmail.com", '04023', "password", '111')
#     patient2.set_user()

# dict_users = system.get_users()
# dict_centres = system.get_centres()

# print("USERS++++++++++++++++++++")
# for key in dict_users:
#     print(dict_users[key])

# for key in dict_centres:
#     print(dict_centres[key])
# print("END++++++++++++++++++++++")

# app1 = Appointment(system.generate_appointment_id(), "usr-581793", "usr-277879", "c-125704", "12/10/18", "1400")
# app1.set_appointment()
# app1 = Appointment(system.generate_appointment_id(), "usr-900458", "usr-277879", "c-125704", "12/10/18", "1400")
# app1.set_appointment()
# user = system.get_user("sid@gmail.com")

# appointments = system.get_appointments()

# print(user)

# for key in appointments:
#     print(appointments[key].appointmentID + appointments[key].time)
# rating1 = Rating("H", "T", 3)
# rating2 = Rating("H", "K", 2)
# list_ratings = [rating1, rating2]
# system.set_ratings(list_ratings)
# ratings = system.get_ratings()

# for i in ratings:
#     print(i.rating + i.patientID + i.entityID)

# centre = system.get_centre("c-902450")

# print(centre.name)
note = system.get_note("n-76950")
print(note.body)