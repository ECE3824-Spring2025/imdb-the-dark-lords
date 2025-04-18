# app.py
from flask import Flask, render_template, request, jsonify, session
import requests
from database_connect import cursor
from flask_caching import Cache
import Movie
from routes import *
from utilities import *

app = Flask(__name__)  # define flask app

# configuration
app.secret_key = 'your_secret_key'  # secret key for session management and security

# Import routes after app is defined
from routes import *

if __name__ == "__main__":
    app.run(debug=True)  # run the app in debug mode for development

fav_movies = []  # list to store favorite movies

app.config['CACHE_TYPE'] = 'SimpleCache'  # set cache type again 
app.config['CACHE_DEFAULT_TIMEOUT'] = 600  # set cache timeout
cache = Cache(app)  # reinitialize cache 

# fetching posters
OMDB_API_KEY = 'e6d88f23'  # omdb api key for fetching movie data
def get_movie_poster(imdb_id):
    url = f'http://www.omdbapi.com/?i={imdb_id}&apikey={OMDB_API_KEY}'# build request url
    response = requests.get(url) # send request to omdb api
    data = response.json() # parse response json
    return data.get('Poster', 'https://www.omdbapi.com/?i=tt3896198&apikey=e6d88f23') # return poster or fallback

# cache this functions result for 10 minutes under a fixed key
@cache.cached(timeout=600, key_prefix='top_movies')

def fetch_top_movies():
    movies = [] # list to hold movie objects
    query = ("SELECT * FROM `database`" "ORDER BY `averageRating` DESC") # sql query to get top rated movies
    cursor.execute(query) # execute query
    rows = cursor.fetchall() # fetch all rows

    # create movie objects from each row and add to list
    for tconst, _, primaryTitle, originalTitle, isAdult, startYear, _, runtimeMinutes, genres, averageRating, numVotes in rows:
        movies.append(Movie.Movie(tconst, primaryTitle, originalTitle, isAdult, startYear, runtimeMinutes, genres, averageRating, numVotes))
    return movies # return list of movie objects

# route to test top movie fetching
@app.route('/test', methods=['GET', 'POST'])
def test():
    movies = fetch_top_movies()  # get top movies
    for movie in movies[:10]: # print first 10 to console
        print(movie)

# cache function based on genre parameter (memoize allows dynamic caching)
@cache.memoize(timeout=600)  # Cache based on function arguments
def fetch_movies_by_genre(genre):
    movies_rating = [] # list for top rated movies by genre
    movies_votes = [] # list for most voted movies by genre

    # query top rated/votes movies
    query_rating = f"SELECT * FROM `database` WHERE FIND_IN_SET('{genre}', `genres`) > 0 ORDER BY `averageRating` DESC LIMIT 10"
    query_votes = f"SELECT * FROM `database` WHERE FIND_IN_SET('{genre}', `genres`) > 0 ORDER BY `numVotes` DESC LIMIT 10"

    cursor.execute(query_rating) # execute rating query
    rows = cursor.fetchall()# fetch results
    for tconst, _, primaryTitle, originalTitle, isAdult, startYear, _, runtimeMinutes, genres, averageRating, numVotes in rows:
        movies_rating.append(Movie.Movie(tconst, primaryTitle, originalTitle, isAdult, startYear, runtimeMinutes, genres, averageRating, numVotes))

    cursor.execute(query_votes) # execute rating query
    rows = cursor.fetchall()# fetch results
    for tconst, _, primaryTitle, originalTitle, isAdult, startYear, _, runtimeMinutes, genres, averageRating, numVotes in rows:
        movies_votes.append(Movie.Movie(tconst, primaryTitle, originalTitle, isAdult, startYear, runtimeMinutes, genres, averageRating, numVotes))

    return movies_rating, movies_votes# return both lists
"""
def root():
    if 'username' in session:
        return redirect(url_for('index_func'))  # go to the homepage with movies
    return redirect(url_for('login'))  # otherwise, show login
"""
# main index route to display movies by genre
@app.route('/', methods=['GET', 'POST'])
def index_func():
    isnew = False

    if "username" in session:   

        # return row of user 
        row = load_user(session["username"])  

        # check if this is a new session 
        if row[0][2]==1: # CHECKS IF ITS NEW ACCOUNT   

            # replace with not new 
            save_user(row[0][0],row[0][1],0)
            isnew = True
        
        genre = request.args.get('genre')  # get genre from query string
        rating_data, likes_data = [], []  # initialize data lists
        if genre:
            rating_data, likes_data = fetch_movies_by_genre(genre.capitalize())  # fetch movies by genre
        for movie in rating_data:
            movie.poster = get_movie_poster(movie.tconst)  # get poster for top-rated
        for movie in likes_data:
            movie.poster = get_movie_poster(movie.tconst)  # get poster for most-voted
        # render page with data
        print(session["username"])
        return render_template("index.html", new_account = isnew, genre=genre, rating_data=rating_data, likes_data=likes_data, favs_data=fav_movies)
    else: 
        return redirect(url_for('login'))

# route to add a movie to favorites
@app.route('/add_favorite', methods=['POST'])
def add_favorite():
    movie_data = request.json# get json data from request
    current_movies = [m['id'] for m in fav_movies]# get current favorite movie ids
    if not (movie_data['id'] in current_movies): # if not already in list
        fav_movies.append(movie_data) # add movie to favorites
        return jsonify({"status": "success","append": True})
    return jsonify({"status": "success","append": False})# already exists, no change

# route to remove a movie from favorites
@app.route('/remove_favorite', methods=['POST'])
def remove_favorite():
    movie_id = request.json['id'] # get movie id from request
    fav_movies[:] = [m for m in fav_movies if m['id'] != movie_id]   # filter out the removed movie
    return jsonify({"status": "success"})
