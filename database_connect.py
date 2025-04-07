import mysql.connector
import Movie

config = {
  'user': 'admin',
  'password': 'IMDB123456789',
  'host': 'darklord-database.cfwkee8cwe1v.us-east-1.rds.amazonaws.com',    # Hostname only
  'port': 3306,           # Default MySQL port for MAMP is 8889
  'database': 'IMDB',
  'raise_on_warnings': True,
}

link = mysql.connector.connect(**config)
cursor = link.cursor()
'''
movies = []

query = ("SELECT * FROM `database`" "ORDER BY `averageRating` DESC")

if link.is_connected():
  print("✅ Successfully connected to the 'movies_data' database.")
else:
#     print("❌ Connection failed.")

cursor.execute(query)
rows = cursor.fetchall()

for tconst, _, primaryTitle, originalTitle, isAdult, startYear, _, runtimeMinutes, genres, averageRating, numVotes in rows:
    movies.append(Movie.Movie(tconst, primaryTitle, originalTitle, isAdult, startYear, runtimeMinutes, genres, averageRating, numVotes))

for movie in movies[-10:]:
    print(movie)
'''