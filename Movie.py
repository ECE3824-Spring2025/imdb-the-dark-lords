class Movie:
    def __init__(self, tconst, primaryTitle, originalTitle, isAdult, startYear, runtimeMinutes, genres, averageRating, numVotes):
        self.tconst = tconst
        self.primaryTitle = primaryTitle
        self.originalTitle = originalTitle
        self.isAdult = isAdult
        self.startYear = startYear
        self.runtimeMinutes = runtimeMinutes
        self.genres = genres
        self.averageRating = averageRating
        self.numVotes = numVotes

    def __str__(self):
        return f"ID: {self.tconst}, English Title: {self.primaryTitle}, Original Title: {self.originalTitle}, R-rated: {self.isAdult}, Year: {self.startYear}, Duration: {self.runtimeMinutes} minutes, Genres: {self.genres}, Rating: {self.averageRating} ({self.numVotes} votes)"