# app.py
from flask import Flask, render_template, request, jsonify
import sort_data
import favs_list

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index_func():
    genre = request.args.get('genre')  # 'comedy', 'drama', 'action', or None
    rating_data = None
    likes_data = None
    favs_data = favs_list.fav_movies

    if genre == 'comedy':
        rating_data = sort_data.sorted_ListWithRatingComedy_NoRepeats
        likes_data  = sort_data.sorted_ListWithLikesComedy_NoRepeats

    elif genre == 'drama':
        rating_data = sort_data.sorted_ListWithRatingDrama_NoRepeats
        likes_data  = sort_data.sorted_ListWithLikesDrama_NoRepeats

    elif genre == 'action':
        rating_data = sort_data.sorted_ListWithRatingAction_NoRepeats
        likes_data  = sort_data.sorted_ListWithLikesAction_NoRepeats

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
    if movie_data not in favs_list.fav_movies:
        favs_list.fav_movies.append(movie_data)
    return jsonify({"status": "success"})

@app.route('/remove_favorite', methods=['POST'])
def remove_favorite():
    movie_id = request.json['id']
    favs_list.fav_movies = [m for m in favs_list.fav_movies if m['id'] != movie_id]
    return jsonify({"status": "success"})




if __name__ == "__main__":
    app.run(debug=True)
