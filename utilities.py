from werkzeug.security import generate_password_hash, check_password_hash  # for securely hashing and verifying passwords
from database_connect import cursor
from database_connect import link

# function returns all rows from for a user
# RETURNS LIST OF TUPLE
# INDEX row[0][N] 
def load_user(user):

    # query to select entire users table
    query = (f"SELECT * FROM `users` WHERE `user` = \"{user}\"")
    cursor.execute(query) 

    # return users table from cursor
    row = cursor.fetchall() 
    return row

# commits a user to the SQL table
def save_user(username, password, isnew):

    # insert with SQL query 
    query = (f"REPLACE INTO `users` (user, password, isnew) VALUES (\"{username}\",\"{password}\",\"{isnew}\")")
    cursor.execute(query) 

    # save database
    link.commit()

# function to register a new user
def register_user(username, password):

    # rewrite code to check prexisting list with the find command
    row = load_user(username) 

    # exit if user exists
    if row:
        return False
    
    # create user if it down not exist
    else:

        # create password from hash 
        hashed_pw = generate_password_hash(password)    

        # call save function
        save_user(username,hashed_pw,1)                 

        # exit gracefully 
        return True  

# authenticate by returning user info from SQL table
def authenticate_user(username, password):

    # call user function 
    row = load_user(username)

    # check if user exists 
    if row:

        # perform password check
        if check_password_hash(row[0][1], password): 

            # authenticate true if correct
            return True  

    # return false if password is wrong or user does not exist   
    return False  