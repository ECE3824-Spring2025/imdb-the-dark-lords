ListWithRatingDrama=[{"id": "tt0068646", "name": "The Godfather", "rating":9.2}, 
{"id": "tt0468569", "name": "The Dark Knight", "rating":9.0},
{"id": "tt0060196", "name": "The Good, the Bad and the Ugly", "rating":8.8},
{"id": "tt0110912", "name": "Pulp Fiction", "rating":8.9},
{"id": "tt0068646", "name": "The Godfather", "rating":9.2},
{"id": "tt0111161", "name": "The Shawshank Redemption", "rating": 9.3}, 
{"id": "tt0050083", "name": "12 Angry Men", "rating":9.0},
{"id": "tt0167260", "name": "The Lord of the Rings: The Return of the King", "rating":9.0},
{"id": "tt0109830", "name": "Forrest Gump", "rating":8.8},
{"id": "tt0108052", "name": "Schindler's List", "rating":9.0}]


# Remove duplicates by 'id'
ListWithRatingDrama_NoRepeats = {movie['id']: movie for movie in ListWithRatingDrama}.values()
sorted_movies = sorted(ListWithRatingDrama_NoRepeats, key=lambda x: x['rating'], reverse=True)

for i in sorted_movies:
    print(i)
