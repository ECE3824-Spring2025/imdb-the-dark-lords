# app.py
from flask import Flask, render_template, request
import movie_data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index_func():
    genre = request.args.get('genre')  # 'comedy', 'drama', 'action', or None
    rating_data = None
    likes_data = None

    if genre == 'comedy':
        rating_data = movie_data.sorted_ListWithRatingComedy_NoRepeats
        likes_data  = movie_data.sorted_ListWithLikesComedy_NoRepeats

    elif genre == 'drama':
        rating_data = movie_data.sorted_ListWithRatingDrama_NoRepeats
        likes_data  = movie_data.sorted_ListWithLikesDrama_NoRepeats

    elif genre == 'action':
        rating_data = movie_data.sorted_ListWithRatingAction_NoRepeats
        likes_data  = movie_data.sorted_ListWithLikesAction_NoRepeats

    return render_template(
        "index.html", 
        genre=genre, 
        rating_data=rating_data, 
        likes_data=likes_data
    )

if __name__ == "__main__":
    app.run(debug=True)
