from flask import render_template, request, redirect, flash, url_for, jsonify  # import essential flask utilities
from werkzeug.security import generate_password_hash, check_password_hash  # for securely hashing and verifying passwords
import json  # for reading and writing user data as json
from app import app  # import the flask app instance from app.py
from flask import session  # import session to manage user login state
from utilities import *

# route for the login and registration page (combined page)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  # if the form was submitted
        if 'signup' in request.form:  # if signup hidden input is present, it's a registration attempt
            username = request.form['username']  # get the username from the form
            password = request.form['password']  # get the password from the form

            if register_user(username, password):  # try to register the user
                flash('Registration successful! Please log in.')  # show a success message
                return redirect(url_for('login'))  # redirect back to login form
            else:
                flash('Username already taken.')  # show an error if username exists
                return redirect(url_for('login'))  # stay on the login page

        else:  # otherwise, it's a login attempt
            username = request.form['username']  # get the username from the form
            password = request.form['password']  # get the password from the form

            if authenticate_user(username, password):  # check if login is valid
                session['username'] = username  # store the username in session
                return redirect(url_for('index_func'))  # redirect to the home page
            else:
                flash('invalid username or password.')  # show an error message
    
    return render_template('login.html')  # render the login/register combined page

# route for the homepage
@app.route('/')
def home():
    if 'username' not in session:  # check if the user is not logged in
        return redirect(url_for('login'))  # redirect them to login
    return redirect(url_for('index_func'))  # if logged in, go to home page
