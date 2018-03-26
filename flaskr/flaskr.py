"""
Program Name: flaskr
By: Omer Alon
Date: 20/02/17
Program Version: 1.0.0
"""
import user
import ctypes
import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

# constants
FLASK_SETTINGS = "FLASKR_SETTINGS"
LOGIN_PAGE = "login_screen.html"
LOGIN_BOX = "login_box.html"
REGISTER_PAGE = "registration_screen.html"
REGISTER_BOX = "registration_box.html"
TEAM_SELECTION_PAGE = "team_selection_screen"
HOME_PAGE = "home_screen"
GET = "GET"
POST = "POST"
USERNAME = "username"
PASSWORD = "password"


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


@app.route('/')
def login():
    """Present the Login page."""
    return render_template(LOGIN_PAGE)


@app.route('/check_user', methods=[GET, POST])
def check_user():
    """Check if the user exists in the database."""
    # get the input
    set_user(request.form[USERNAME], request.form[PASSWORD])
    # check if the user exists in the database
    if my_user.match_password():
        my_user.load_teams()
        return render_template(HOME_PAGE)
    # present an error message box.
    else:
        return render_template(LOGIN_BOX)


@app.route('/not_registered', methods=[GET, POST])
def not_registered():
    """Send him to the registration page."""
    return render_template(REGISTER_PAGE)


@app.route('/new_user_details', methods=[GET, POST])
def new_user_details():
    """Confirm that the new user's username and password
       are not in use."""
    # get the input
    set_user(request.form[USERNAME], request.form[PASSWORD])
    # check if the details are already exist
    if my_user.check_details():
        return render_template(REGISTER_BOX)
    else:
        return render_template(TEAM_SELECTION_PAGE)


def set_user(username, password):
    """set the user's attributes


    Receives:
        username - A string which contains the username of the current user
        password - A string which contains the password of the current user
    """
    my_user.set_username(username)
    my_user.set_password(password)


app.run()



