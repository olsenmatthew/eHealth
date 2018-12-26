from flask import Flask, redirect, request, render_template, url_for, Response, abort, flash
from flask_login import LoginManager, login_user, current_user, login_required, logout_user, UserMixin
from datetime import datetime
from time import time
import calendar
from app.modules.level_0.class_system import *
from app.modules.level_1.class_user import *
from app.modules.level_1.class_appointment import *
from app.modules.level_1.class_note import *

# -------------------------------------------------------------------------------------------------
# App Initiate
# -------------------------------------------------------------------------------------------------
app = Flask(__name__)


# -------------------------------------------------------------------------------------------------
# Import Routes
# -------------------------------------------------------------------------------------------------
@app.route('/')  # maps a url to a return value of a function
@app.route('/<username>')
def index(username=None):
    return render_template("visitor/home.html", username=username)


# -------------------------------------------------------------------------------------------------
# Login routes
# -------------------------------------------------------------------------------------------------
# Configure login manager
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'secretKey'


@login_manager.user_loader
def load_user(id):
    system = System
    return system.get_user(id)


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login?next=' + request.path)


@app.route('/login', methods=['POST', 'GET'])
@app.route('/login/<username>')
def login():
    system = System
    error = None
    if request.method == "POST":
        email = request.form["email"]
        user = system.get_user(email)
        if user == None:
            error = 'email'
            return render_template("visitor/login.html", error=error)
        elif user._type == 'provider':
            if user.password != request.form["password"]:
                error = 'password'
                return render_template("visitor/login.html", error=error)
            login_user(user)
            return redirect(url_for("provider_home", username=current_user.name))
        elif user._type == 'patient' and user.password == request.form["password"]:
            if user.password != request.form["password"]:
                error = 'password'
                return render_template("visitor/login.html", error=error)
            login_user(user)
            return redirect(url_for("patient_home", username=current_user.name))
    return render_template("visitor/login.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


# -------------------------------------------------------------------------------------------------
# Register routes
# -------------------------------------------------------------------------------------------------
@app.route('/register', methods=['POST', 'GET'])
def register(error=None):
    system = System
    error = {"name": "", "surname": "", "phone": "", "email": "", "medicareNo": "", \
             "pass1": "", "pass2": "", "pass_match": "", "user_exists": ""}
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        phone = request.form["phone"]
        email = request.form["email"]
        medicareNo = request.form["medicareNo"]
        pass1 = request.form["pass1"]
        pass2 = request.form["pass2"]
        if name == "":
            error["name"] = "name_empty"
        if surname == "":
            error["surname"] = "surname_empty"
        if phone == "":
            error["phone"] = "phone_empty"
        if email == "":
            error["email"] = "email_empty"
        if medicareNo == "":
            error["medicareNo"] = "medicareNo_empty"
        if pass1 == "":
            error["pass1"] = "pass1_empty"
        if pass2 == "":
            error["pass2"] = "pass2_empty"
        if pass1 != pass2:
            error["pass_match"] = "pass_match"
        if system.get_user(email) is not None:
            error["user_exists"] = "user_exists"
        for key in error:
            if error[key] is not "":
                return render_template("visitor/register.html", error=error)
        user = Patient(system.generate_user_id(), name, surname, email, phone, \
                       pass1, medicareNo)
        user.set_user()
        login_user(user)
        return render_template("patient/home.html", error=None)
    error = "input"
    return render_template("visitor/register.html", error=error)


# -------------------------------------------------------------------------------------------------
# Provider routes 
# -------------------------------------------------------------------------------------------------
@app.route('/provider/<username>')
@login_required
def provider_home(username=None):
    return render_template("provider/home.html", username=username)


@app.route('/provider/<username>/profile')
@login_required
def provider_profile(username=None):
    return render_template("provider/profile/profile.html", username=username)


@app.route('/provider/<username>/profile')
@app.route('/provider/<username>/profile/myinfo', methods=['POST', 'GET'])
@login_required
def provider_info(username=None, error=None):
    system = System
    if request.method == "POST":
        if request.form['name'] != '':
            current_user.name = request.form['name']
        if request.form['surname'] != '':
            current_user.surname = request.form['surname']
        if request.form['phone'] != '':
            current_user.phone_number = request.form['phone_num']
        if request.form['email'] != '':
            if system.get_user(request.form['email']) is None:
                current_user.email = request.form['email']
            else:
                error = "user exists"
        if request.form['providerNo'] != '':
            current_user.providerNo = request.form['providerNo']
        if request.form['profession'] != '':
            current_user.profession = request.form['profession']
        current_user.set_user()
    return render_template("provider/profile/myinfo.html", username=username, error=error)


@app.route('/provider/<username>/profile')
@app.route('/provider/<username>/profile/mypassword', methods=['POST', 'GET'])
@login_required
def provider_password(username=None):
    if request.method == "POST":
        password = request.form["pass"]
        new_pass1 = request.form["new_pass1"]
        new_pass2 = request.form["new_pass2"]
        if password == "":
            message = 'Please enter password!'
            return render_template('provider/profile/mypassword.html', username=username, message=message)
        if password != current_user.password:
            message = 'Incorrect password!'
            return render_template('provider/profile/mypassword.html', username=username, message=message)
        if new_pass1 == "":
            message = 'Please enter new password!'
            return render_template('provider/profile/mypassword.html', username=username, message=message)
        if new_pass1 != new_pass2:
            message = 'Passwords did not match!'
            return render_template('provider/profile/mypassword.html', username=username, message=message)
        message = 'Password Updated!'
        current_user.password = new_pass1
        current_user.set_user()
        return render_template('provider/profile/mypassword.html', username=username, message=message)
    return render_template("provider/profile/mypassword.html", username=username)


@app.route('/provider/<username>/appointments')
@login_required
def provider_appointments(username=None, appointments=None, system=None):
    system = System
    appointments = current_user.get_appointments()
    appointments.sort()
    return render_template("provider/appointments/appointments.html", username=username, appointments=appointments)


@app.route('/provider/<username>/patients')
@login_required
def provider_patients(username=None):
    patients = current_user.get_patients()
    return render_template("provider/patients/patients.html", username=username, patients=patients)


@app.route('/provider/<username>/patients')
@app.route('/provider/<username>/patients/search', methods=['POST', 'GET'])
@login_required
def provider_patients_search(username=None):
    if request.method == "POST":
        search = request.form['patient']
        current_user.get_patients()
        patients = []
        for i in current_user.patients:
            user = get_user(i)
            patients.append(user)
        return render_template("provider/patients/patients_search.html", username=username, patients=patients)


@app.route('/provider/<username>/patient_<patient_id>')
@login_required
def provider_patient_profile(username=None, patient=None, patient_id=None):
    system = System
    patient = system.get_user(patient_id)
    return render_template("provider/patients/patients_profile.html", username=username, patient=patient, \
                           patient_id=patient_id)

@app.route('/provider/<username>/patient_<patient_id>/prev_notes', methods = ["POST", "GET"])
@app.route('/provider/<username>/patient_<patient_id>/prev_notes/edit=<edit>', methods = ["POST", "GET"])
@app.route('/provider/<username>/patient_<patient_id>/prev_notes/delete=<delete>', methods = ["POST", "GET"])
@login_required
def provider_patient_notes(username=None, patient_id=None, delete=None, edit=None):
    system = System
    patient = system.get_user(patient_id)
    provider = system.get_user(current_user.userID)
    if request.method == "POST":
        note = system.get_note(edit)
        edit=None
        time_view = datetime.now()
        time_view = time_view.strftime("%d/%m/%y %H:%M")
        epoch_time = calendar.timegm(datetime.now().timetuple())
        note = Note(note.notesID, note.provider, note.patient, time_view, epoch_time, request.form["body"])
        note.set_note()
    if delete != None:
        note = system.get_note(delete)
        note.delete_note()
    patient_notes = patient.get_notes()
    patient_notes.sort()
    return render_template("provider/patients/notes.html", username=username, patient=patient, \
                           patient_id=patient_id, patient_notes=patient_notes, edit=edit)

@app.route('/provider/<username>/patient_<patient_id>/new_note', methods=['POST', 'GET'])
@login_required
def provider_patient_new_note(username=None, patient=None, patient_id=None, notes_id=None):
    system = System
    message=None
    patient = system.get_user(patient_id)
    provider = system.get_user(current_user.userID)
    time_view = datetime.now()
    time_view = time_view.strftime("%d/%m/%y %H:%M")
    epoch_time = calendar.timegm(datetime.now().timetuple())
    if request.method == "POST":
        note = Note(system.generate_note_id(), provider, patient, time_view, epoch_time, request.form["body"])
        note.set_note()
        message="saved"
    return render_template("provider/patients/new_note.html", username=username, patient=patient, \
                           patient_id=patient_id, notes_id=notes_id, message=message)
# -------------------------------------------------------------------------------------------------
# Patient Routes
# -------------------------------------------------------------------------------------------------
@app.route('/patient/<username>')
@login_required
def patient_home(username=None):
    return render_template("patient/home.html", username=username)


@app.route('/patient/<username>/profile')
@login_required
def patient_profile(username=None):
    return render_template("patient/profile/profile.html", username=username)


@app.route('/patient/<username>/appointments', methods=['POST', 'GET'])
@app.route('/patient/<username>/appointments/delete=<delete>', methods=['POST', 'GET'])
@login_required
def patient_appointments(username=None, delete=None):
    system = System
    if delete != None:
        app = system.get_appointment(delete)
        app.delete_appointment()
    appointments = current_user.get_appointments()
    appointments.sort()
    return render_template("patient/appointments/appointments.html", username=username, appointments=appointments)


@app.route('/patient/<username>/profile/myinfo', methods=['POST', 'GET'])
@login_required
def patient_info(username=None, error=None):
    system = System
    if request.method == "POST":
        if request.form['name'] != '':
            current_user.name = request.form['name']
        if request.form['surname'] != '':
            current_user.surname = request.form['surname']
        if request.form['phone_num'] != '':
            current_user.phone = request.form['phone_num']
        if request.form['email'] != '':
            if system.get_user(request.form['email']) is None:
                current_user.email = request.form['email']
            else:
                error = "user exists"
        if request.form['medicare_num'] != '':
            current_user.medicareNo = request.form['medicare_num']
        current_user.set_user()
    return render_template("patient/profile/myinfo.html", username=username, error=error)


@app.route('/patient/<username>/profile/changepassword', methods=['POST', 'GET'])
@login_required
def patient_password(username=None):
    if request.method == "POST":
        if request.form['pass'] == '':
            message = 'Please enter password!'
        elif request.form['pass'] != current_user.password:
            message = 'Incorrect password!'
        elif request.form['new_pass_1'] == '':
            message = 'Please enter new password!'
        elif request.form['new_pass_1'] != request.form['new_pass_2']:
            message = 'Passwords did not match!'
        else:
            message = 'Password Updated!'
            current_user.password = request.form['new_pass_1']
            current_user.set_user()
        return render_template('patient/profile/mypassword.html', username=username, message=message)
    return render_template("patient/profile/mypassword.html", username=username)


@app.route('/patient/<username>/search_centres', methods=['POST', 'GET'])
@login_required
def patient_search_centre(username=None):
    system = System
    dict_centres = system.get_centres()
    error=None
    centres = []
    centres_filterd = []
    for key in dict_centres:
        centres.append(dict_centres[key])
    if request.method == "POST":
        search = request.form["search"]
        for c in centres:
            if search.lower() in c.name.lower():
                centres_filterd.append(c)
        centres = centres_filterd
        if centres == []:
            error = search
    return render_template("patient/search/search_centre.html", username=username, centres=centres, error=error)


@app.route('/patient/<username>/search_locations', methods=['POST', 'GET'])
@login_required
def patient_search_location(username=None):
    system = System
    error = None
    dict_centres = system.get_centres()
    centres = []
    centres_filterd = []
    for key in dict_centres:
        centres.append(dict_centres[key])
    if request.method == "POST":
        search = request.form["search"]
        for c in centres:
            if search.lower() in c.location.lower():
                centres_filterd.append(c)
        centres = centres_filterd
        if centres == []:
            error = search
    return render_template("patient/search/search_location.html", username=username, centres=centres, error=error)


@app.route('/patient/<username>/search_services', methods=['POST', 'GET'])
@login_required
def patient_search_service(username=None):
    system = System
    error = None
    dict_users = system.get_users()
    providers = []
    providers_filtered = []
    for key in dict_users:
        if dict_users[key]._type == "provider":
            providers.append(dict_users[key])
    if request.method == "POST":
        search = request.form["search"]
        for p in providers:
            if search.lower() in p.profession.lower():
                providers_filtered.append(p)
        providers = providers_filtered
        if providers == []:
            error = search
    return render_template("patient/search/search_service.html", username=username, providers=providers, error=error)


@app.route('/patient/<username>/search_providers', methods=['POST', 'GET'])
@login_required
def patient_search_provider(username=None):
    system = System
    error = None
    dict_users = system.get_users()
    providers = []
    providers_filtered = []
    for key in dict_users:
        if dict_users[key]._type == "provider":
            providers.append(dict_users[key])
    if request.method == "POST":
        search = request.form["search"]
        for p in providers:
            if search.lower() in p.name.lower() or search.lower() in p.surname.lower():
                providers_filtered.append(p)
        providers = providers_filtered
        if providers == []:
            error = search
    return render_template("patient/search/search_provider.html", username=username, providers=providers, error=error)


@app.route('/patient/<username>/centre_<centre_id>', methods=['POST', 'GET'])
@login_required
def patient_centre_profile(username=None, centre_id=None):
    system = System
    error = None
    centre = system.get_centre(centre_id)
    providers = centre.get_providers()
    services = []
    
    # Creating a list of services that the centre provides
    for p in providers:
        isListed = False
        for s in services:
            if p.profession == s:
                isListed = True
        if isListed == False:
            services.append(p.profession)

    # If a rating is submitted, check if it is between 0 and 5 and if it is not retrun an error message 
    if request.method == "POST":
        rating = request.form['rating']
        if int(rating) < 0 or int(rating) > 5:
            error = "invalid rating"
        else:
            current_user.rate(int(rating), centre.centreID)
    return render_template("patient/centre_profile/centre_profile.html", username=username, centre=centre, \
    services=services, error=error)


@app.route('/patient/<username>/centre_<centre_id>/<service>', methods=['POST', 'GET'])
@login_required
def patient_centre_services(username=None, centre_id=None, service=None):
    system = System
    centre = system.get_centre(centre_id)
    providers = centre.get_providers()
    providers_filtered = []
    for p in providers:
        if p.profession == service:
            providers_filtered.append(p)
    providers = providers_filtered
    return render_template("patient/centre_profile/centre_services.html", username=username, centre=centre, \
                           providers=providers, service=service)

@app.route('/patient/<username>/centre_<centre_id>/book_provider_id=<provider_id>', methods=['POST', 'GET'])
@login_required
def patient_centre_services_book(username=None, centre_id=None, provider_id=None):
    system = System
    message = None
    patient = system.get_user(current_user.userID)
    provider = system.get_user(provider_id)
    centre = system.get_centre(centre_id)
    time_slots = ['8:30 AM','8:45 AM','9:00 AM','9:15 AM','9:30 AM','9:45 AM','10:00 AM','10:15 AM','10:30 AM','10:45 AM','11:00 AM','11:15 AM', \
    '11:30 AM','11:45 AM','12:00 PM','12:15 PM','12:30 PM','12:45 PM', '1:00 PM','1:15 PM','1:30 PM','1:45 PM','2:00 PM','2:15 PM','2:30 PM','2:45 PM', \
    '3:00 PM','3:15 PM','3:30 PM','3:45 PM','4:00 PM','4:15 PM','4:30 PM','4:45 PM', '5:00 PM', '5:30 PM']

    if request.method == "POST":
        date = request.form["date"]
        time = request.form.get("time")
        date_time = str(date + " " + time)
        try:
            date_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M %p")
            epoch_time = calendar.timegm(date_time.timetuple())
            date_time = date_time.strftime("%d/%m/%y %H:%M %p")
            now = calendar.timegm(datetime.now().timetuple())
            if epoch_time < now:
                message = "Invalid date"
            else:
                appID = system.generate_appointment_id()
                appointment = Appointment(appID, patient, provider, centre, date_time, epoch_time)
                message = appointment.set_appointment()   
        except:
            message = "No date"
    return render_template("patient/centre_profile/centre_services_book.html", username=username, provider=provider, \
                           centre=centre, time_slots=time_slots, message=message)

@app.route('/patient/<username>/provider_<provider_id>', methods=['POST', 'GET'])
@login_required
def patient_provider_profile(username=None, provider_id=None):
    system = System
    error = None
    provider = system.get_user(provider_id)
    centres = provider.get_centres()
    if request.method == "POST":
        rating = request.form['rating']
        if int(rating) < 0 or int(rating) > 5:
            error = "invalid rating"
        else:
            current_user.rate(int(rating), provider.userID)
    return render_template("patient/provider_profile/provider_profile.html", username=username, provider=provider, \
                           centres=centres, error=error)


@app.route('/patient/<username>/provider_<provider_id>/book_centre_id=<centre_id>', methods=['POST', 'GET'])
@login_required
def patient_provider_profile_book(username=None, provider_id=None, centre_id=None):
    system = System
    message = None
    patient = system.get_user(current_user.userID)
    provider = system.get_user(provider_id)
    centre = system.get_centre(centre_id)
    time_slots = ['8:30 AM','8:45 AM','9:00 AM','9:15 AM','9:30 AM','9:45 AM','10:00 AM','10:15 AM','10:30 AM','10:45 AM','11:00 AM','11:15 AM', \
    '11:30 AM','11:45 AM','12:00 PM','12:15 PM','12:30 PM','12:45 PM', '1:00 PM','1:15 PM','1:30 PM','1:45 PM','2:00 PM','2:15 PM','2:30 PM','2:45 PM', \
    '3:00 PM','3:15 PM','3:30 PM','3:45 PM','4:00 PM','4:15 PM','4:30 PM','4:45 PM', '5:00 PM', '5:30 PM']

    if request.method == "POST":
        date = request.form["date"]
        time = request.form.get("time")
        date_time = str(date + " " + time)
        try:
            date_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M %p")
            epoch_time = calendar.timegm(date_time.timetuple())
            date_time = date_time.strftime("%d/%m/%y %H:%M %p")
            now = calendar.timegm(datetime.now().timetuple())
            if epoch_time < now:
                message = "Invalid date"
            else:
                appID = system.generate_appointment_id()
                appointment = Appointment(appID, patient, provider, centre, date_time, epoch_time)
                message = appointment.set_appointment()   
        except:
            message = "No date"
    return render_template("patient/centre_profile/centre_services_book.html", username=username, provider=provider, \
                           centre=centre, time_slots=time_slots, message=message)
# -------------------------------------------------------------------------------------------------
# App Run
# -------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001)
