from app.modules.level_0.class_system import *
from app.modules.level_1.class_user import *
from app.modules.level_1.class_centre import *
from app.modules.level_1.class_appointment import *
from app.modules.level_0.class_rating import *
from app.modules.level_1.class_note import *
from datetime import datetime
from time import time
import calendar

system = System

print("########################################          START         ########################################")

# test cases for patients
# making a new patient with name sam gibbs whose email is s@gmail.com and phoneNo 04023 and pass is 111
patient1 = Patient(system.generate_user_id(), "sam", "gibbs", "s@gmail.com", '04023', "password", '111')
patient1.set_user()

# making sure the patient is not NULL
assert patient1 is not None, "patient object error"
print("passed patient creation test")

# capitalizing the patient first name and it is same is sam
assert patient1.name == "sam".capitalize(), "patient name error"
print("passed patient name test")

# capitalizing patient last name and it is same as gibbs
assert patient1.surname == "gibbs".capitalize(), "patient surname error"
print("passed patient surname test")

# making sure the email is same as what he entered
assert patient1.email == "s@gmail.com", "patient email error"
print("passed patient email test")

# making sure the patient id is not NULL
assert patient1.userID is not None, "patient UID error"
print("passed patient userID test")

# patient password is matches
assert patient1.password == "password", "patient password error"
print("passed patient password test")

# phone number is matches
assert patient1.phone == "04023", "patient phone error"
print("passed patient phone test")

# medicareNo is same as he entered
assert patient1.medicareNo == "111", "patient medicare number error"
print("passed patient medicareNo test")

# the system returns the patient1 when his email is entered
assert system.get_user("s@gmail.com") == patient1, "system.get_user is not returning the correct object"
print("passed system.get_user test")

# deleting patient1
patient1.delete_user()

# making sure the patient credentials has been deleted
assert system.get_user("s@gmail.com") is None, "system.delete_user is not deleting the user"
print("passed system.delete_user test")

# making a patient2 with name Harold Newman with email h@gmail.com phoneNo 04023 Password as password and medicareNo
# as 111
patient2 = Patient(system.generate_user_id(), "Harold", "Newman", "h@gmail.com", '04023', "password", '111')
patient2.set_user()

# making sure the email matches the email of patient2
assert system.get_user("h@gmail.com") == patient2, "Harold Newman user was not created"
print("passed system.get_user user test")

# recreating the patient2 as patient3 wiht similar info
patient3 = Patient(system.generate_user_id(), "Harold", "Newman", "h@gmail.com", '04023', "password", '111')

# if patient3 is not NULL the error should be displayed as a patient cannot be created twice
assert patient3 is not None, "User Generated Twice"
print("passed recreation of user test")

# deleting patient3
patient3.delete_user()

# searching for h@gmail.com and it should not delete harold newman
assert system.get_user("h@gmail.com") is not None, "system.delete_user deleted user without proper instantiation"
print("passed recreation of user test")

# assigning harld newman to as patient2
patient2 = system.get_user("h@gmail.com")

# deleting patient2
patient2.delete_user()
print("passed delete user test")

# creating patient4 with name ali babar with email babar@gmail.com phone 0421 password as pass and medicareNo as 131
patient4 = Patient(system.generate_user_id(), "ali", "babar", "babar@gmail.com", '0421', "pass", '131')
patient4.set_user()

# making sure patient4 is not NuLL
assert patient4 is not None, "patient object error"
print("passed patient creation test")

# capitalizing the first name of the patient
assert patient4.name == "ali".capitalize(), "patient name error"
print("passed patient name test")

# capitalizing the last name of the patient
assert patient4.surname == "babar".capitalize(), "patient surname error"
print("passed patient surname test")

# making sure the patient email is same as what he entered
assert patient4.email == "babar@gmail.com", "patient email error"
print("passed patient email test")

# making sure that the patient is assigned an id
assert patient4.userID is not None, "patient UID error"
print("passed patient userID test")

# patient password is pass
assert patient4.password == "pass", "patient password error"
print("passed patient password test")

# phone number is same as what he entered
assert patient4.phone == "0421", "patient phone error"
print("passed patient phone test")

# medicareNo is 131
assert patient4.medicareNo == "131", "patient medicare number error"
print("passed patient medicareNumber test")

# in system his email is returning the right value
assert system.get_user("babar@gmail.com") == patient4, "system.get_user is not returning the correct object"
print("passed system.get_user test")

# deleting patient4
patient4.delete_user()

# search for patient4 after deletion and the system should return Null as it was previous deleted
assert system.get_user("babar@gmail.com") is None, "system.delete_user is not deleting the user"
print("passed system.delete_user test")

# assigning dict_users to system.get_user
dict_users = system.get_users()

# making sure dict_users has been assigned values
assert dict_users != {}, "system.get_users error, not returning users"

# looping through dict_users and making sure that it is not Null
for i in dict_users:
    assert i is not None, "system.get_users error, not returning users"
    assert i != {}, "system.get_users error, not returning instantiated users"
print("passed delete user from dict test")

# all the tests for patients has passed
print("==========Passed test cases for patients==========")

# test cases for providers making a provider1 whose name is gibbons reed with email gr@gmail.com phoneNo 6101335429
# and password as password and provider id as 939 and specialty in plastic surgery
provider1 = Provider(system.generate_user_id(), "gibbons", "reed", "gr@gmail.com", "6101335429", "password", "939", \
                     "plastic surgeon")
provider1.set_user()

# making sure the user is not NULL
assert provider1 is not None, "patient object error"
print("passed provider creation test")

# making sure the provider first name is gibbons in capitals
assert provider1.name == "gibbons".capitalize(), "provider name error"
print("passed provider name creation test")

# making sure the provider last name is reed in capitals
assert provider1.surname == "reed".capitalize(), "provider surname error"
print("passed provider surname creation test")

# making sure his email is correct
assert provider1.email == "gr@gmail.com", "provider email error"
print("passed provider email creation test")

# making sure his number is also correct
assert provider1.phone == "6101335429", "patient phone error"
print("passed provider phone creation test")

# he should be provided with an Id and it shouldn't be Null
assert provider1.userID is not None, "provider UID error"
print("passed provider userID creation test")

# making sure his password is same as what he provided
assert provider1.password == "password", "provider password error"
print("passed provider password creation test")

# and his providerNO is 939
assert provider1.providerNo == "939", "provider number error"
print("passed provider providerNo creation test")

# making sure the his profession is plastic surgeon in capitals
assert provider1.profession == "plastic surgeon".capitalize(), "provider profession error"
print("passed provider profession creation test")

# when his userId is inserted the system should return provider1
assert system.get_user(provider1.userID) == provider1, "system.get_user is not returning the correct object"
print("passed provider UID creation test")

# deleting provider1
provider1.delete_user()

# making sure the deletion is successful
assert system.get_user(provider1.userID) is None, "system.delete_user is not deleting user"
print("passed provider deletion from system test")

print("===========Passed test cases for providers===========")

# test cases for centres

# if not system.get_centre("15311"):
# making a Hospital with abnNo 15311 name Matthews Hospital phoneNO 5107335429 location at Merica
matthews_hospital = Centre(system.generate_centre_id(), "15311", "Matthews Hospital", \
                           "Hospital", "5107335429", "Merica")

# making sure matthews_hospital is not NULL
assert matthews_hospital is not None, "Error is creating centre"
print("passed create centre test")

# making the abn is same as what he entered
assert matthews_hospital.abn == "15311", "error centre abn"
print("passed create centre abn test")

# making sure the name is Matthew Hospital capitalized
assert matthews_hospital.name == "Matthews Hospital".capitalize(), "error centre name"
print("passed create centre name test")

# making sure the phoneNO is same as what he entered
assert matthews_hospital.phone == "5107335429", "error centre phone number"
print("passed create centre phone test")

# making sure it is located in Merica
assert matthews_hospital.location == "Merica", "error centre location"
print("passed create centre location test")

dict_centres = system.get_centres()

# looping through dict_centres and making sure it NULL
for i in dict_centres:
    assert i is not None, "system.get_centres error in objects in dict_centres"
    print("passed centre in system test")
    assert i != {}, "system.get_centres error, not returning correct centres"
    print("passed centre data in system test")

new_centres = []

# looping through centres dictionaries
# appending the centres ID that are not same as mathew Hospital Id to new_centres
for i in dict_centres:
    if i != matthews_hospital.centreID:
        new_centres.append(i)

system.set_centres(new_centres)

dict_centres = system.get_centres()

# looping through dict_centres
# making sure that matthews_hospital id is not in it
for i in dict_centres:
    assert i != matthews_hospital.centreID, "did not properly remove centre"
    print("passed centre properly deleted from system test")

# all tests for centers passed
print("=========Passed test cases for centres==========")

# test cases for notes
time = datetime.now()
epoch = calendar.timegm(datetime.now().timetuple())

# making a note that consists of id provider patient time, age and reads as this is my note
note = Note(system.generate_note_id(), provider1, patient1, time, epoch, "This is my note")

# making sure not is not NULL
assert note is not None, "note not created"
print("passed note creation test")

# making the provider on note is same as provider1
assert note.provider == provider1, "create note provider error"
print("passed note provider test")

# making sure the paitent on note is same as patient
assert note.patient == patient1, "create note patient error"
print("passed note patient test")

# making sure the time is similar to the note time
assert note.time_view == time, "create note view time error"
print("passed note time_view test")

# making sure his epoch or age is similar
assert note.epoch_time == epoch, "create note epoch time error"
print("passed note epoch_time test")

# note should read "this is my note"
assert note.body == "This is my note", "create note body error"
print("passed note body test")

note.set_note()

note2 = system.get_note(note.notesID)

# making sure note2 is not NULL
assert note2 is not None, "system get note error"

# the note2 and not should have same values as they are equal
assert note2.provider == note.provider, "system returned unequal notes(provider) error"
print("passed system note provider equal test")

# the values of note2 patient and note patient are same
assert note2.patient == note.patient, "system returned unequal notes(patient) error"
print("passed system note patient equal test")

# the values of note2 time_view and time_view note are same
assert note2.time_view == note.time_view, "system returned unequal notes(time_view) error"
print("passed system note time_view equal test")

# the values of note2 epoch_time and note epoch_time are same
assert note2.epoch_time == note.epoch_time, "system returned unequal notes(epoch) error"
print("passed system note epoch_time equal test")

# the values of note2 body and note body are same
assert note2.body == note.body, "system returned unequal notes(body) error"
print("passed system note body equal test")

# the values of note2.notesID and note.notesID are same
assert note2.notesID == note.notesID, "system returned unequal notes(notesID) error"
print("passed system note notesID equal test")

# deleting note
note.delete_note()

# making sure the delete was successful
assert system.get_note(note.notesID) is None, "deleting notes error"
print("passed system delete note from database test")

all_notes = system.get_notes()

# looping through all notes
# making sure x is not NULL
# and values inside it are not same as note
for x in all_notes:
    assert x is not None, "error returning system notes"
    print("passed system storage of notes")
    assert x != note.notesID, "did not delete note from database"

print("passed system delete note from database test")

# all test for notes passed
print("==========Passed test cases for notes==========")


# test cases for rating
# instantiate ratings object
rating = Rating(patient1, matthews_hospital, 5)
assert rating is not None, "system creating rating error"
print("passed rating instantiation test")

# check that rating object.patientID is equal to initializing value
assert rating.patientID == patient1, "system creating rating patientID error"
print("passed rating patientID instantiation test")

# check that rating object.entityID is equal to initializing value
assert rating.entityID == matthews_hospital, "system creating rating entityID error"
print("passed rating entityID instantiation test")

# check that rating object.rating is equal to initializing value
assert rating.rating == 5, "system creating rating rate error"
print("passed rating stars instantiation test")

print("==========Passed test cases for rating==========")

# test cases for appointments
# instantiate appointment object
appointment = Appointment(system.generate_appointment_id(), patient1, provider1, matthews_hospital, time, epoch)

# make sure that instantiation occured correctly
assert appointment is not None, "creating appointment error"
print("passed appointment instantiation test")

# make sure that appointment object patient patient is initialized correctly
assert appointment.patient == patient1, "creating appointment patient error"
print("passed appointment patient instantiation test")

# make sure that appointment object patient provider is initialized correctly
assert appointment.provider == provider1, "creating appointment provider error"
print("passed appointment provider instantiation test")

# make sure that appointment object patient centre is initialized correctly
assert appointment.centre == matthews_hospital, "creating appointment centre error"
print("passed appointment centre instantiation test")

# make sure that appointment object patient date_time is initialized correctly
assert appointment.date_time == time, "creating appointment date_time error"
print("passed appointment date_time instantiation test")

# make sure that appointment object epoch_time attribute is initialized correctly
assert appointment.epoch_time == epoch, "creating appointment epoch error"
print("passed appointment epoch_time instantiation test")

# save appointment to system
appointment.set_appointment()

# test that appointments are in appointment list in DB
appointment2 = system.get_appointment(appointment.appointmentID)
assert appointment2 is not None, "system returned null appointment error"
print("passed system appointment retrieval test")

# test that object returned contains same patient attribute data
assert appointment2.patient == appointment.patient, "system returned incorrect appointment error"
print("passed system appointment patient equal test")

# test that object returned contains same provider attribute data
assert appointment2.provider == appointment.provider, "system returned incorrect appointment error"
print("passed system appointment provider equal test")

# test that object returned contains same date_time attribute data
assert appointment2.date_time == appointment.date_time, "system returned incorrect appointment error"
print("passed system appointment date_time equal test")

# test that object returned contains same epoch_time attribute data
assert appointment2.epoch_time == appointment.epoch_time, "system returned incorrect appointment error"
print("passed system appointment epoch_time equal test")

# get all appointments from systems
appointments = system.get_appointments()

# test that appointment is in database
for i in appointments:
    assert i != appointment.appointmentID, "system appointment error"
print("passed system set item in list test")

# test that system can retrieve selected appointment from database
assert system.get_appointment(appointment.appointmentID) is not None, "system appointment error"
print("passed system set item in list test")

# test that system the retrieved selected appointment attribute is the same as the object instantiated
assert system.get_appointment(appointment.appointmentID).appointmentID == appointment.appointmentID, "system object " \
                                                                                                     "error "
# test that system the retrieved selected appointment attribute is the same as the object instantiated
print("passed system get appointment ID in list test")

# test that system the retrieved selected appointment patient attribute is the same as the object instantiated
assert system.get_appointment(appointment.appointmentID).patient == appointment.patient, "system object error"
print("passed system get appointment patient in list test")

# test that system the retrieved selected appointment provider attribute is the same as the object instantiated
assert system.get_appointment(appointment.appointmentID).provider == appointment.provider, "system object error"
print("passed system get appointment provider in list test")

# test that system the retrieved selected appointment date_time attribute is the same as the object instantiated
assert system.get_appointment(appointment.appointmentID).date_time == appointment.date_time, "system object error"
print("passed system get appointment date_time in list test")

# test that system the retrieved selected appointment epoch_time attribute is the same as the object instantiated
assert system.get_appointment(appointment.appointmentID).epoch_time == appointment.epoch_time, "system object error"
print("passed system get appointment epoch_time in list test")

print("==========Passed test cases for appointments==========")

print("########################################          FINISH         ########################################")


