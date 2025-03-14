# app.py
from flask import Flask, render_template, request, jsonify
import requests
#import sort_data
#import favs_list
from database_connect import cursor #database cursor to execute queries
from flask_caching import Cache #for caching
import Movie #for movie objects

fav_movies = [] #list to store faves
app = Flask(__name__) # definng flask app

app.config['CACHE_TYPE'] = 'SimpleCache'  #use in-memory caching
app.config['CACHE_DEFAULT_TIMEOUT'] = 600  #cache expires after 10 minutes
cache = Cache(app)


OMDB_API_KEY = 'e6d88f23' #API key

def get_movie_poster(imdb_id):
    url = f'http://www.omdbapi.com/?i={imdb_id}&apikey={OMDB_API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data.get('Poster', 'https://www.omdbapi.com/?i=tt3896198&apikey=e6d88f23') #default poster url if not found

@cache.cached(timeout=600, key_prefix='top_movies') #caching top movies data for 10 mins
def fetch_top_movies():
    movies = []
    query = "SELECT * FROM `database` ORDER BY `COL 10` DESC" #sort by votes
    cursor.execute(query)
    rows = cursor.fetchall()

    #movie objects and ass to list
    for tconst, _, primaryTitle, originalTitle, isAdult, startYear, _, runtimeMinutes, genres, averageRating, numVotes in rows:
        movies.append(Movie.Movie(tconst, primaryTitle, originalTitle, isAdult, startYear, runtimeMinutes, genres, averageRating, numVotes))

    return movies

@app.route('/test', methods=['GET', 'POST'])
def test():
    movies = fetch_top_movies()
    for movie in movies[:10]:
        print(movie)

@cache.memoize(timeout=600)  #cache genre-based movie search results
def fetch_movies_by_genre(genre):
    movies_rating = [] #store top rated movies
    movies_votes = [] #store top voted movies

    #SQL queries to fetch top rated and voted movies of each genre
    query_rating = f"SELECT * FROM `database` WHERE FIND_IN_SET('{genre}', `genres`) > 0 ORDER BY `averageRating` DESC LIMIT 10"
    query_votes = f"SELECT * FROM `database` WHERE FIND_IN_SET('{genre}', `genres`) > 0 ORDER BY `numVotes` DESC LIMIT 10"

    cursor.execute(query_rating)
    rows = cursor.fetchall()
    for tconst, _, primaryTitle, originalTitle, isAdult, startYear, _, runtimeMinutes, genres, averageRating, numVotes in rows:
        movies_rating.append(Movie.Movie(tconst, primaryTitle, originalTitle, isAdult, startYear, runtimeMinutes, genres, averageRating, numVotes))

    cursor.execute(query_votes)
    rows = cursor.fetchall()
    for tconst, _, primaryTitle, originalTitle, isAdult, startYear, _, runtimeMinutes, genres, averageRating, numVotes in rows:
        movies_votes.append(Movie.Movie(tconst, primaryTitle, originalTitle, isAdult, startYear, runtimeMinutes, genres, averageRating, numVotes))

    return movies_rating, movies_votes


@app.route('/', methods=['GET', 'POST'])
def index_func():
    genre = request.args.get('genre')  #get genre from requested
    rating_data, likes_data = [], [] #lists to store movie data

    if genre:
        rating_data, likes_data = fetch_movies_by_genre(genre.capitalize())

    #fetch posters for movies in rating and likes data
    for movie in rating_data:
        movie.poster = get_movie_poster(movie.tconst)

    for movie in likes_data:
        movie.poster = get_movie_poster(movie.tconst)

    return render_template("index.html", genre=genre, rating_data=rating_data, likes_data=likes_data, favs_data=fav_movies)


@app.route('/add_favorite', methods=['POST'])
def add_favorite():
    movie_data = request.json
    current_movies = [m['id'] for m in fav_movies] #extract existing favorite movie IDs
    if not (movie_data['id'] in current_movies): #only add if not already in favorites
        fav_movies.append(movie_data)
        return jsonify({"status": "success","append": True})
    return jsonify({"status": "success","append": False})

@app.route('/remove_favorite', methods=['POST'])
def remove_favorite():
    movie_id = request.json['id']
    fav_movies[:] = [m for m in fav_movies if m['id'] != movie_id]  #modify list in-place
    return jsonify({"status": "success"})

@app.route('/clear-cache')
def clear_cache():
    cache.clear()
    return "Cache cleared!"


if __name__ == "__main__":
    app.run(debug=True)
