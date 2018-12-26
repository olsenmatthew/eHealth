from flask import Flask, redirect, request, render_template, url_for, Response, abort, flash, app
from flask_login import LoginManager, login_user, current_user, login_required, logout_user, UserMixin
from app.modules.level_0.class_system import *
from app.modules.level_1.class_user import *
from app.modules.level_1.class_appointment import *
from app.modules.level_1.class_centre import *


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
@login_required
def patient_appointments(username=None):
    system = System
    if request.method == "POST":
        if request.form['del_id'] != '':
            del_id = request.form['del_id']
            appointment = Appointment(del_id, None, None, None, None, None)
            appointment.delete_appointment()
            appList = system.get_appointments()
            return render_template("patient/appointments/appointments.html", username=username, appList=appList)

    appList = system.get_appointments()
    return render_template("patient/appointments/appointments.html", username=username, appList=appList)


@app.route('/patient/<username>/bookings', methods=['POST', 'GET'])
@login_required
def patient_bookings(username=None):
    return render_template("patient/appointments/bookings.html", username=username)


@app.route('/patient/<username>/profile/myinfo', methods=['POST', 'GET'])
@login_required
def patient_info(username=None):
    system = System
    if request.method == "POST":
        first_name = ''
        surname = ''
        phone_number = ''
        medicare_number = ''
        if request.form['name'] != '':
            first_name = request.form['name']
        if request.form['surname'] != '':
            surname = request.form['surname']
        if request.form['phone_num'] != '':
            phone_number = request.form['phone_num']
        if request.form['medicare_num'] != '':
            medicare_number = request.form['medicare_num']
        if request.form['name'] != '' and request.form['surname'] != '' and request.form['phone_num'] != '' and \
                request.form['medicare_num'] != '':
            mUser = User(username, first_name, surname, phone_number, medicare_number)
            mUser.set_user()
        # else: error message
        return render_template("patient/profile/myinfo.html", username=username)


@app.route('/patient/<username>/profile/changepassword', methods=['POST', 'GET'])
@login_required
def patient_password(username=None):
    system = System
    if request.method == "POST":
        if request.form['pass'] == '':
            message = 'Please enter password!'
        elif request.form['pass'] != current_user.password:
            message = 'Incorrect password!'
        elif request.form['new_pass_1'] == '':
            message = 'Please enter new password!'
        elif request.form['new_pass_1'] != request.form['new_pass_2']:
            message = 'Passwords do not match!'
        else:
            message = 'Password Updated!'

        if message == 'Password Updated!':
            mUser = system.get_user(username)
            userID = mUser[list("userID")[0]]
            name = mUser[list("name")[0]]
            surname = mUser[list("surname")[0]]
            email = mUser[list("email")[0]]
            phone = mUser[list("phone")[0]]
            password = request.form['new_pass_1']

            xUser = User(userID, name, surname, email, phone, password)
            xUser.set_user()

        return render_template('patient/profile/mypassword.html', username=username, message=message)
    return render_template("patient/profile/mypassword.html", username=username)


@app.route('/patient/<username>/search_centres', methods=['POST', 'GET'])
@login_required
def patient_search_centre(username=None):
    system = System
    if request.method == "POST":
        search = request.form['search']

        # TODO: IF NEEDED CHANGE LATER IN ORDER TO RETRIEVE MULTIPLE CENTRES
        centres = system.get_centre(search)

        return render_template("patient/search/search_centre.html", username=username, centres=centres)
    else:
        centres = system.get_centres()
        return render_template("patient/search/search_centre.html", username=username, centres=centres)


# TODO: CREATE LOCATION FUNCTIONS IN SYSTEM
@app.route('/patient/<username>/search_locations', methods=['POST', 'GET'])
@login_required
def patient_search_location(username=None):
    system = System
    if request.method == "POST":
        search = request.form['search']

        locations = []
        centres = system.get_centres()
        for centre in centres:
            if search.lower() in centre.location.lower():
                locations.append(centre)

        return render_template("patient/search/search_location.html", username=username, locations=locations)
    else:
        locations = system.get_centres()
        return render_template("patient/search/search_location.html", username=username, locations=locations)


@app.route('/patient/<username>/search_services', methods=['POST', 'GET'])
@login_required
def patient_search_service(username=None):
    system = System
    if request.method == "POST":
        search = request.form['search']

        providers = []
        users = system.get_users()
        for user in users:
            if "pr-" in user.userID.lower():
                providers.append(user)

        services = []
        for provider in providers:
            if search.lower() in provider.profession.lower():
                services.append(provider)

        return render_template("patient/search/search_service.html", username=username, services=services)
    else:
        providers = []
        users = system.get_users()
        for user in users:
            if "pr-" in user.userID.lower():
                providers.append(user)
        services = providers
        return render_template("patient/search/search_service.html", username=username, services=services)


@app.route('/patient/<username>/search_providers', methods=['POST', 'GET'])
@login_required
def patient_search_provider(username=None):
    system = System
    if request.method == "POST":
        search = request.form['search']

        providers = []
        users = system.get_users()
        for user in users:
            if "pr-" in user.userID.lower():
                providers.append(user)

        providers = []
        for provider in providers:
            if search.lower() in provider.name.lower() or search.lower() in provider.surname.lower():
                providers.append(provider)

        return render_template("patient/search/search_provider.html", username=username, providers=providers)
    else:

        providers = []
        users = system.get_users()
        for user in users:
            if "pr-" in user.userID.lower():
                providers.append(user)

        return render_template("patient/search/search_provider.html", username=username, providers=providers)


@app.route('/patient/<username>/centre_<centre_id>', methods=['POST', 'GET'])
@login_required
def patient_centre_profile(username=None, centre=None, centre_id=None, error=None):
    system = System
    centre = system.get_centre(centre_id)
    centre.get_providers()
    if request.method == "POST":
        rating = request.form['rating']
        if int(rating) < 0 or int(rating) > 5:
            error = 'invalid rating'
        else:  # TODO: MAKE SURE THAT THE CORRECT PREVIOUS RATING IF IT EXISTS IS REMOVED, USE PREFIXES
            m_ratings = system.get_ratings()
            new_ratings = []
            previous_rating = []
            for r in m_ratings:
                if centre_id in r and username in r:
                    previous_rating.append(r)
                else:
                    new_ratings.append(r)
            previous_rating = [centre_id, username, rating]  # reset previous rating to input rating
            new_ratings.append(previous_rating)
            system.set_ratings(new_ratings)  # TODO: DEBUG HERE
    return render_template("patient/centre_profile/centre_profile.html", username=username, \
                           centre=centre, centre_id=centre.id, error=error)


@app.route('/patient/<username>/centre_<centre_id>/<service>', methods=['POST', 'GET'])
@login_required
def patient_centre_services(username=None, centre=None, centre_id=None, service=None, providers=None):
    system = System
    centre = system.get_centre(centre_id)
    providers = centre.get_providers()

    filtered_providers = []
    for provider in providers:
        if service.lower() in provider:
            filtered_providers.append(provider)

    return render_template("patient/centre_profile/centre_services.html", username=username, centre=centre, \
                           centre_id=centre.id, service=service, providers=filtered_providers)


@app.route('/patient/<username>/provider_<provider_id>', methods=['POST', 'GET'])
@login_required
def patient_provider_profile(username=None, provider=None, provider_id=None, centre=None, error=None):
    system = System
    provider = system.get_user(provider_id)
    centre_names = provider.get_centres()
    centres = []
    for c in centre_names:
        centres.append(system.get_centre(c))
    if request.method == "POST":
        rating = request.form['rating']
        if int(rating) < 0 or int(rating) > 5:
            error = 'invalid rating'
        else:  # TODO: MAKE SURE THAT THE CORRECT PREVIOUS RATING IF IT EXISTS IS REMOVED, USE PREFIXES  
            m_ratings = system.get_ratings()
            new_ratings = []
            previous_rating = []
            for r in m_ratings:
                if provider_id in r and username in r:
                    previous_rating.append(r)
                else:
                    new_ratings.append(r)
            previous_rating = [provider_id, username, rating]  # reset previous rating to input rating
            new_ratings.append(previous_rating)
            system.set_ratings(new_ratings)  # TODO: DEBUG HERE
    return render_template("patient/provider_profile/provider_profile.html", username=username, provider=provider, \
                           provider_id=provider.id, centres=centres, error=error)
