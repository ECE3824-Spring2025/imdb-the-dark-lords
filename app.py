# app.py
from flask import Flask, render_template, request, jsonify
import requests
#import sort_data
#import favs_list
from database_connect import cursor
import Movie
fav_movies = []
app = Flask(__name__) # definng flask app

OMDB_API_KEY = 'e6d88f23'

def get_movie_poster(imdb_id):
    url = f'http://www.omdbapi.com/?i={imdb_id}&apikey={OMDB_API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data.get('Poster', 'https://www.omdbapi.com/?i=tt3896198&apikey=e6d88f23')

@app.route('/test', methods=['GET', 'POST'])
def test():
    movies = []
    query = ("SELECT * FROM `database`" "ORDER BY `COL 10` DESC")
    cursor.execute(query)
    rows = cursor.fetchall()

    for tconst, _, primaryTitle, originalTitle, isAdult, startYear, _, runtimeMinutes, genres, averageRating, numVotes in rows:
        movies.append(Movie.Movie(tconst, primaryTitle, originalTitle, isAdult, startYear, runtimeMinutes, genres, averageRating, numVotes))

    for movie in movies[:10]:
        print(movie)

@app.route('/', methods=['GET', 'POST'])
def index_func():
    genre = request.args.get('genre')  # 'comedy', 'drama', 'action', or None
    rating_data = []
    likes_data = []
    favs_data = []

    #favs_data = [favs_list.fav_movies]

    if genre == 'comedy':
        movies_rating = []
        movies_votes = []
        query_rating = ("SELECT * FROM `database` WHERE FIND_IN_SET('Comedy', `genres`) > 0 ORDER BY `averageRating` DESC LIMIT 10")
        query_votes = ("SELECT * FROM `database` WHERE FIND_IN_SET('Comedy', `genres`) > 0 ORDER BY `numVotes` DESC LIMIT 10")
        cursor.execute(query_rating)
        rows = cursor.fetchall()
        for tconst, _, primaryTitle, originalTitle, isAdult, startYear, _, runtimeMinutes, genres, averageRating, numVotes in rows:
            movies_rating.append(Movie.Movie(tconst, primaryTitle, originalTitle, isAdult, startYear, runtimeMinutes, genres, averageRating, numVotes))

        cursor.execute(query_votes)
        rows = cursor.fetchall()
        for tconst, _, primaryTitle, originalTitle, isAdult, startYear, _, runtimeMinutes, genres, averageRating, numVotes in rows:
            movies_votes.append(Movie.Movie(tconst, primaryTitle, originalTitle, isAdult, startYear, runtimeMinutes, genres, averageRating, numVotes))

        rating_data = movies_rating
        likes_data  = movies_votes

    elif genre == 'drama':
        movies_rating = []
        movies_votes = []
        query_rating = ("SELECT * FROM `database` WHERE FIND_IN_SET('Drama', `genres`) > 0 ORDER BY `averageRating` DESC LIMIT 10")
        query_votes = ("SELECT * FROM `database` WHERE FIND_IN_SET('Drama', `genres`) > 0 ORDER BY `numVotes` DESC LIMIT 10")
        cursor.execute(query_rating)
        rows = cursor.fetchall()
        for tconst, _, primaryTitle, originalTitle, isAdult, startYear, _, runtimeMinutes, genres, averageRating, numVotes in rows:
            movies_rating.append(Movie.Movie(tconst, primaryTitle, originalTitle, isAdult, startYear, runtimeMinutes, genres, averageRating, numVotes))

        cursor.execute(query_votes)
        rows = cursor.fetchall()
        for tconst, _, primaryTitle, originalTitle, isAdult, startYear, _, runtimeMinutes, genres, averageRating, numVotes in rows:
            movies_votes.append(Movie.Movie(tconst, primaryTitle, originalTitle, isAdult, startYear, runtimeMinutes, genres, averageRating, numVotes))

        rating_data = movies_rating
        likes_data  = movies_votes


    elif genre == 'action':
        movies_rating = []
        movies_votes = []
        query_rating = ("SELECT * FROM `database` WHERE FIND_IN_SET('Action', `genres`) > 0 ORDER BY `averageRating` DESC LIMIT 10")
        query_votes = ("SELECT * FROM `database` WHERE FIND_IN_SET('Action', `genres`) > 0 ORDER BY `numVotes` DESC LIMIT 10")
        cursor.execute(query_rating)
        rows = cursor.fetchall()
        for tconst, _, primaryTitle, originalTitle, isAdult, startYear, _, runtimeMinutes, genres, averageRating, numVotes in rows:
            movies_rating.append(Movie.Movie(tconst, primaryTitle, originalTitle, isAdult, startYear, runtimeMinutes, genres, averageRating, numVotes))

        cursor.execute(query_votes)
        rows = cursor.fetchall()
        for tconst, _, primaryTitle, originalTitle, isAdult, startYear, _, runtimeMinutes, genres, averageRating, numVotes in rows:
            movies_votes.append(Movie.Movie(tconst, primaryTitle, originalTitle, isAdult, startYear, runtimeMinutes, genres, averageRating, numVotes))

        rating_data = movies_rating
        likes_data  = movies_votes

    for movie in rating_data:
        movie.poster = get_movie_poster(movie.tconst)

    for movie in likes_data:
        movie.poster = get_movie_poster(movie.tconst)

    return render_template(
        "index.html", 
        genre=genre, 
        rating_data=rating_data, 
        likes_data=likes_data,
        favs_data = favs_data
    )

@app.route('/add_favorite', methods=['POST'])
def add_favorite():
    movie_data = request.json
    current_movies = [m['id'] for m in fav_movies]
    if not (movie_data['id'] in current_movies):
        fav_movies.append(movie_data)
        return jsonify({"status": "success","append": True})
    return jsonify({"status": "success","append": False})

@app.route('/remove_favorite', methods=['POST'])
def remove_favorite():
    movie_id = request.json['id']
    fav_movies[:] = [m for m in fav_movies if m['id'] != movie_id]  # Modify list in-place
    return jsonify({"status": "success"})



if __name__ == "__main__":
    app.run(debug=True)
