"""
Program Name: flaskr
By: Omer Alon
Date: 20/02/17
Program Version: 1.0.0
"""
from global_constants import *
import user
import datetime
import threading
import information_server
import time
from teams_data import *
import ctypes
import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, Response

# constants
FLASK_SETTINGS = "FLASKR_SETTINGS"
LOGIN_PAGE = "login_screen.html"
LOGIN_BOX = "login_box.html"
REGISTER_PAGE = "registration_screen.html"
REGISTER_BOX = "registration_box.html"
TEAM_SELECTION_PAGE = "team_selection_screen.html"
HOME_PAGE = "home_screen.html"
LOADING_PAGE = "loading_screen.html"
UPDATE_PAGE = "update_screen.html"
GET = "GET"
POST = "POST"
USERNAME = "username"
PASSWORD = "password"
LIVE = "Live Matches"
FINISHED_MATCHES = "Finished Matches"
FUTURE_MATCHES = "Future Matches"
END_MATCH = "The match was finished. The final score is:"
NEW_MATCH = "New match begun:"
GOAL = "GOOOOOAL for "
ENTHUSIASM = " ! ! ! The score is:"
LIVE_MESSAGE = "There are no live matches for your teams right now"
FINISHED_MESSAGE = "There are no finished matches yet"
FUTURE_MESSAGE = "Future matches have not scheduled yet"
SKIP = "skip"


# create the application instance :)
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY="development key",
    USERNAME="Boomeralon",
    PASSWORD="0274"
))
app.config.from_envvar(FLASK_SETTINGS, silent=True)

# initialize the user object
my_user = user.User("", "")
live = []
finished = []
future = []
updates = []
current_page = ""


@app.route('/')
def login():
    """Present the Login page."""
    global my_user
    my_user = user.User("", "")
    return render_template(LOGIN_PAGE)


@app.route('/check_user', methods=[GET, POST])
def check_user():
    """Check if the user exists in the database."""
    # get the input
    set_user(request.form[USERNAME], request.form[PASSWORD])
    # check if the user exists in the database
    if my_user.match_password():
        my_user.load_teams()
        return render_template(LOADING_PAGE, tryit=my_user)
    # present an error message box.
    else:
        return render_template(LOGIN_BOX)


@app.route('/not_registered', methods=[GET, POST])
def not_registered():
    """Send the user to the registration page."""
    return render_template(REGISTER_PAGE)


@app.route('/new_user_details', methods=[GET, POST])
def new_user_details():
    """Confirm that the new user's username and password
       are not in use."""
    global my_user
    # get the input
    set_user(request.form[USERNAME], request.form[PASSWORD])
    # check if the details are already exist
    if my_user.check_details():
        return render_template(REGISTER_BOX)
    else:
        return team_selection_screen()


@app.route('/team_selection_screen', methods=[GET, POST])
def team_selection_screen():
    """Present the team selection page."""
    global my_user
    all_teams = information_server.InformationSource.get_all_teams()
    return render_template(TEAM_SELECTION_PAGE, teams=all_teams, user_teams=my_user.get_teams)


@app.route('/set_user_teams', methods=[GET, POST])
def set_user_teams():
    """Get the teams that the user chose and set the teams' attribute."""
    chosen_teams = []
    for team in request.form:
        chosen_teams.append(team)
    my_user.set_teams(chosen_teams)
    return render_template(LOADING_PAGE, tryit=my_user)


@app.route('/home', methods=[GET, POST])
def home():
    """Send him to the registration page."""
    global finished, live, future
    for x in request.form:
        print x
    finished, live, future = my_user.get_matches_categorized()
    thread = threading.Thread(target=search_changes)
    thread.start()
    return show_live(False)


@app.route('/show_live', methods=[GET, POST])
def show_live(check_updates=True):
    global current_page, live
    if current_page != LIVE:
        check_updates = False
        current_page = LIVE
    if check_updates:
        return show_update()
    if live:
        present_live = information_server.InformationSource.organize_info(live)
        return render_template(HOME_PAGE, matches=present_live, type=LIVE, func="/show_live")
    else:
        return render_template(HOME_PAGE, message=LIVE_MESSAGE)


@app.route('/show_finished', methods=[GET, POST])
def show_finished(check_updates=True):
    global current_page, finished
    if current_page != FINISHED_MATCHES:
        check_updates = False
        current_page = FINISHED_MATCHES
    if check_updates:
        return show_update()
    if finished:
        present_finished = information_server.InformationSource.organize_info(finished)
        return render_template(HOME_PAGE, matches=present_finished, type=FINISHED_MATCHES)
    else:
        return render_template(HOME_PAGE, message=FINISHED_MESSAGE)


@app.route('/show_future', methods=[GET, POST])
def show_future(check_updates=True):
    global current_page, future
    if current_page != FUTURE_MATCHES:
        check_updates = False
        current_page = FUTURE_MATCHES
    if check_updates:
        return show_update()
    if future:
        present_future = information_server.InformationSource.organize_info(future)
        return render_template(HOME_PAGE, matches=present_future, type=FUTURE_MATCHES)
    else:
        return render_template(HOME_PAGE, message=FUTURE_MESSAGE)


@app.route('/show_update', methods=[GET, POST])
def show_update():
    global updates, current_page
    if updates:
        message = updates[0][0]
        match = updates[0][1]
        del updates[0]
        return render_template(UPDATE_PAGE, message=message, match=match)
    else:
        return '', 204


def set_user(username, password):
    """set the user's attributes


    Receives:
        username - A string which contains the username of the current user
        password - A string which contains the password of the current user
    """
    my_user.set_username(username)
    my_user.set_password(password)


def search_changes():
    global live, finished, future, my_user, current_page, updates
    while True:
        new_matches, ended_matches, new_goals_matches, updated = \
            my_user.get_changes_categorized()
        # if only the minutes changed, present the updated minutes
        if not (new_matches or ended_matches or new_goals_matches):
            if live != updated:
                live = updated
                if current_page == LIVE:
                    show_live(False)
        else:
            live = updated
            for match in ended_matches:
                finished.append(match)
                score = "%s - %s" % (match[HOME_GOALS], match[AWAY_GOALS])
                updates.append([END_MATCH, [match[HOME], score, match[AWAY]]])
            for match in new_matches:
                future = [future_match for future_match in
                          future if future_match[HOME] !=
                          match[HOME] or future_match[DATE].strftime("%d.%m.%y") !=
                          datetime.datetime.today().strftime("%d.%m.%y")]
                score = "%s - %s" % (match[HOME_GOALS], match[AWAY_GOALS])
                updates.append([NEW_MATCH, [match[HOME], score, match[AWAY]]])
            for match in new_goals_matches:
                score = "%s - %s" % (match[HOME_GOALS], match[AWAY_GOALS])
                if match[HOME_NEW_GOAL]:
                    message = GOAL + match[HOME] + ENTHUSIASM
                else:
                    message = GOAL + match[AWAY] + ENTHUSIASM
                updates.append([message, [match[HOME], score, match[AWAY]]])

app.run()



