import mysql.connector
import Movie

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',    # Hostname only
  'port': 3306,           # Default MySQL port for MAMP is 8889
  'database': 'movies_data',
  'raise_on_warnings': True,
}

link = mysql.connector.connect(**config)
cursor = link.cursor()
movies = []



# if link.is_connected():
#     print("✅ Successfully connected to the 'movies_data' database.")
# else:
#     print("❌ Connection failed.")

######################################################################################
# Pull top 10 rated Drama movies
######################################################################################

ListWithRatingDrama = []

DramaRatingQuery = """SELECT * FROM `database` WHERE genres LIKE '%Drama%' ORDER BY averageRating DESC"""

cursor.execute(DramaRatingQuery)
drama_rows = cursor.fetchall()

for tconst, _, primaryTitle, originalTitle, isAdult, startYear, _, runtimeMinutes, genres, averageRating, numVotes in drama_rows:
  movie_dict = {
    'id': tconst,
    'primaryTitle': primaryTitle,
    'originalTitle': originalTitle,
    'isAdult': isAdult,
    'startYear': startYear,
    'runtimeMinutes': runtimeMinutes,
    'genres': genres,
    'rating': averageRating,
    'votes': numVotes
  }
  ListWithRatingDrama.append(movie_dict)

print("Top 10 Drama Movies by Rating:\n" + "-"*35)
for movie in ListWithRatingDrama[:10]:
  print(movie)

######################################################################################
# Pull top 10 voted Drama movies
######################################################################################

ListWithVotingDrama = []

DramaVotingQuery = """SELECT * FROM `database` WHERE genres LIKE '%Drama%' ORDER BY numVotes DESC"""

cursor.execute(DramaVotingQuery)
drama_rows = cursor.fetchall()

for tconst, _, primaryTitle, originalTitle, isAdult, startYear, _, runtimeMinutes, genres, averageRating, numVotes in drama_rows:
  movie_dict = {
    'id': tconst,
    'primaryTitle': primaryTitle,
    'originalTitle': originalTitle,
    'isAdult': isAdult,
    'startYear': startYear,
    'runtimeMinutes': runtimeMinutes,
    'genres': genres,
    'rating': averageRating,
    'votes': numVotes
  }
  ListWithVotingDrama.append(movie_dict)

print("Top 10 Drama Movies by Voting:\n" + "-"*35)
for movie in ListWithVotingDrama[:10]:
  print(movie)

######################################################################################
# Pull top 10 rated Action movies
######################################################################################

ListWithRatingAction = []

ActionRatingQuery = """SELECT * FROM `database` WHERE genres LIKE '%Action%' ORDER BY averageRating DESC"""

cursor.execute(ActionRatingQuery)
action_rows = cursor.fetchall()

for tconst, _, primaryTitle, originalTitle, isAdult, startYear, _, runtimeMinutes, genres, averageRating, numVotes in action_rows:
  movie_dict = {
      'id': tconst,
      'primaryTitle': primaryTitle,
      'originalTitle': originalTitle,
      'isAdult': isAdult,
      'startYear': startYear,
      'runtimeMinutes': runtimeMinutes,
      'genres': genres,
      'rating': averageRating,
      'votes': numVotes
  }
  ListWithRatingAction.append(movie_dict)
print("\nTop 10 Action Movies by Rating:\n" + "-"*36)
for movie in ListWithRatingAction[:10]:
    print(movie)

######################################################################################
# Pull top 10 voted Action movies
######################################################################################

ListWithVotingAction = []

ActionVotingQuery = """SELECT * FROM `database` WHERE genres LIKE '%Action%' ORDER BY numVotes DESC"""

cursor.execute(ActionVotingQuery)
drama_rows = cursor.fetchall()

for tconst, _, primaryTitle, originalTitle, isAdult, startYear, _, runtimeMinutes, genres, averageRating, numVotes in drama_rows:
  movie_dict = {
    'id': tconst,
    'primaryTitle': primaryTitle,
    'originalTitle': originalTitle,
    'isAdult': isAdult,
    'startYear': startYear,
    'runtimeMinutes': runtimeMinutes,
    'genres': genres,
    'rating': averageRating,
    'votes': numVotes
  }
  ListWithVotingAction.append(movie_dict)

print("Top 10 Action Movies by Voting:\n" + "-"*35)
for movie in ListWithVotingAction[:10]:
  print(movie)

######################################################################################
# Pull top 10 rated Comedy movies
######################################################################################

ListWithRatingComedy = []

ComedyRatingQuery = """SELECT * FROM `database` WHERE genres LIKE '%Comedy%' ORDER BY averageRating DESC"""

cursor.execute(ActionRatingQuery)
comedy_rows = cursor.fetchall()

for tconst, _, primaryTitle, originalTitle, isAdult, startYear, _, runtimeMinutes, genres, averageRating, numVotes in comedy_rows:
  movie_dict = {
      'id': tconst,
      'primaryTitle': primaryTitle,
      'originalTitle': originalTitle,
      'isAdult': isAdult,
      'startYear': startYear,
      'runtimeMinutes': runtimeMinutes,
      'genres': genres,
      'rating': averageRating,
      'votes': numVotes
  }
  ListWithRatingComedy.append(movie_dict)
print("\nTop 10 Comedy Movies by Rating:\n" + "-"*36)
for movie in ListWithRatingComedy[:10]:
  print(movie)


######################################################################################
# Pull top 10 voted Comdey movies
######################################################################################

ListWithVotingComedy = []

ComedyVotingQuery = """SELECT * FROM `database` WHERE genres LIKE '%Comedy%' ORDER BY numVotes DESC"""

cursor.execute(ComedyRatingQuery)
comedy_rows = cursor.fetchall()

for tconst, _, primaryTitle, originalTitle, isAdult, startYear, _, runtimeMinutes, genres, averageRating, numVotes in drama_rows:
  movie_dict = {
    'id': tconst,
    'primaryTitle': primaryTitle,
    'originalTitle': originalTitle,
    'isAdult': isAdult,
    'startYear': startYear,
    'runtimeMinutes': runtimeMinutes,
    'genres': genres,
    'rating': averageRating,
    'votes': numVotes
  }
  ListWithVotingComedy.append(movie_dict)

print("Top 10 Comedy Movies by Voting:\n" + "-"*35)
for movie in ListWithVotingComedy[:10]:
  print(movie)

