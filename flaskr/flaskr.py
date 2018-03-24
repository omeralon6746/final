# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


app = Flask(__name__) # create the application instance :)

# Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='Boomeralon',
    PASSWORD='0274'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route('/')
def login():
    return render_template('login_screen.html')

app.run()



