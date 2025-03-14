import sys
import os
sys.path.append('/mnt/c/Users/jdjuk/ece_3824/workspace/imdb-the-dark-lords')
from app import app, fav_movies

# Mock data for testing
MOCK_MOVIE = {
    "id": "tt3896198",
    "title": "Guardians of the Galaxy Vol. 2",
    "year": 2017,
    "rating": 7.6,
    "poster": "https://www.omdbapi.com/?i=tt3896198&apikey=e6d88f23"
}

@pytest.fixture
def client():
    app.config['TESTING'] = True  # Enable test mode for Flask
    with app.test_client() as client:
        app.fav_movies.clear()  # Reset favorites list before each test
        yield client

def test_add_favorite_new_movie(client):
    response = client.post('/add_favorite', json=MOCK_MOVIE)
    
    assert response.status_code == 200
    assert response.json == {"status": "success", "append": True}
    assert MOCK_MOVIE in app.fav_movies

def test_add_favorite_duplicate_movie(client):
    client.post('/add_favorite', json=MOCK_MOVIE)
    response = client.post('/add_favorite', json=MOCK_MOVIE)
    
    assert response.status_code == 200
    assert response.json == {"status": "success", "append": False}
    assert len(app.fav_movies) == 1

def test_remove_favorite_existing_movie(client):
    client.post('/add_favorite', json=MOCK_MOVIE)
    
    response = client.post('/remove_favorite', json={"id": MOCK_MOVIE["id"]})
    
    assert response.status_code == 200
    assert response.json == {"status": "success"}
    assert MOCK_MOVIE not in app.fav_movies

def test_remove_favorite_nonexistent_movie(client):
    response = client.post('/remove_favorite', json={"id": MOCK_MOVIE["id"]})
    
    assert response.status_code == 200
    assert response.json == {"status": "success"}
    assert len(app.fav_movies) == 0
