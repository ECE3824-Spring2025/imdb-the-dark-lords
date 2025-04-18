from flask import render_template, request, redirect, flash, url_for, jsonify  # import essential flask utilities
from werkzeug.security import generate_password_hash, check_password_hash  # for securely hashing and verifying passwords
import json  # for reading and writing user data as json
from app import app  # import the flask app instance from app.py
from flask import session  # import session to manage user login state
from utilities import *
# route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  # if the form was submitted
        username = request.form['username']  # get the username from the form
        password = request.form['password']  # get the password from the form

        if authenticate_user(username, password):  # check if login is valid
            session['username'] = username  # store the username in session
            flash('login successful!')  # show a success message
            return redirect(url_for('home'))  # redirect to the home page
        else:
            flash('invalid username or password.')  # show an error message
    
    return render_template('login.html')  # render the login page

# route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':  # if the form was submitted
        username = request.form['username']  # get the username from the form
        password = request.form['password']  # get the password from the form

        if register_user(username, password):  # try to register the user
            flash('registration successful! please log in.')  # show a success message
            return redirect(url_for('login'))  # redirect to the login page
        else:
            flash('username already taken.')  # show an error if the username exists
    
    return render_template('register.html')  # render the registration page

# route for the homepage
@app.route('/')
def home():
    if 'username' not in session:  # check if the user is not logged in
        return redirect(url_for('login'))  # redirect them to login
    return render_template("index.html", username=session['username'])  # render homepage with username
