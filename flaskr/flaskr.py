# all the imports

import user
import ctypes
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash


app = Flask(__name__)  # create the application instance :)

# Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='Boomeralon',
    PASSWORD='0274'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

my_user = user.User("", "")


@app.route('/')
def login():
    return render_template('login_screen.html')


@app.route('/check_user', methods=['GET', 'POST'])
def check_user():
    # get the input
    set_user(request.form["username"], request.form["password"])
    # check if the user exists in the database
    if my_user.match_password():
        my_user.load_teams()
        return render_template('home_screen')
    # present an error message box.
    else:
        return render_template('message_box.html', message="Wrong Username or Password!")


@app.route('/not_registered', methods=['GET', 'POST'])
def not_registered():
    """"If the user is not registered,
        send him to the registration page."""


@app.route('/new_user_details', methods=['GET', 'POST'])
def new_user_details():
    """"If the user is not registered,
        send him to the registration page."""
    set_user(request.form["username"], request.form["password"])
    if my_user.check_details():
        return render_template('message_box.html', message="The username or password are already exist! Try to log in")
    else:
        return render_template('team_selection_screen')


def set_user(username, password):
    my_user.set_username(username)
    my_user.set_password(password)


app.run()



