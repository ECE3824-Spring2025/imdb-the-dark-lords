from werkzeug.security import generate_password_hash, check_password_hash  # for securely hashing and verifying passwords
import json  # for reading and writing user data as json

# function to load users from a json file
def load_users():
    try:
        with open('users.json', 'r') as f:  # open the users file in read mode
            return json.load(f)  # load and return the json data
    except FileNotFoundError:  # if the file doesn't exist
        return {}  # return an empty dictionary

# function to save users to a json file
def save_users(users):
    with open('users.json', 'w') as f:  # open the users file in write mode
        json.dump(users, f)  # write the users dictionary to the file

# function to register a new user
def register_user(username, password):
    users = load_users()  # get the current list of users

    if username in users:  # check if the username is already taken
        return False  # registration fails if the user exists

    hashed_pw = generate_password_hash(password)  # hash the user's password
    users[username] = {'password': hashed_pw, 'new_acct':True}  # store the hashed password under the username
    save_users(users)  # save the updated users list
    return True  # registration was successful

# function to authenticate a user during login
def authenticate_user(username, password):
    users = load_users()  # load the current users

    user = users.get(username)  # get the user data for the given username
    if user and check_password_hash(user['password'], password):  # check if the password is correct
        return True  # return true if login is successful
    return False  # return false if login fails