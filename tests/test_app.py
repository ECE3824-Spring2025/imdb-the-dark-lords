import pytest
from app import app, fav_movies

# Mock data for testing
MOCK_MOVIE = {
    "id": "tt1375666",
    "title": "Inception",
    "year": 2010,
    "rating": 8.8,
    "poster": "https://example.com/inception.jpg"
}

@pytest.fixture
def client():
    app.config['TESTING'] = True  # Enable test mode for Flask
    with app.test_client() as client:
        fav_movies.clear()  # Reset favorites list before each test
        yield client

def test_add_favorite_new_movie(client):
    response = client.post('/add_favorite', json=MOCK_MOVIE)
    
    assert response.status_code == 200
    assert response.json == {"status": "success", "append": True}
    assert MOCK_MOVIE in fav_movies

def test_add_favorite_duplicate_movie(client):
    client.post('/add_favorite', json=MOCK_MOVIE)
    response = client.post('/add_favorite', json=MOCK_MOVIE)
    
    assert response.status_code == 200
    assert response.json == {"status": "success", "append": False}
    assert len(fav_movies) == 1

def test_remove_favorite_existing_movie(client):
    client.post('/add_favorite', json=MOCK_MOVIE)
    
    response = client.post('/remove_favorite', json={"id": MOCK_MOVIE["id"]})
    
    assert response.status_code == 200
    assert response.json == {"status": "success"}
    assert MOCK_MOVIE not in fav_movies

def test_remove_favorite_nonexistent_movie(client):
    response = client.post('/remove_favorite', json={"id": MOCK_MOVIE["id"]})
    
    assert response.status_code == 200
    assert response.json == {"status": "success"}
    assert len(fav_movies) == 0
