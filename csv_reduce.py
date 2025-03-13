import sys
import csv
from itertools import chain

# paths for tsv files
RATINGS = "/home/abryant/database/title.ratings.tsv"
BASICS   = "/home/abryant/database/title.basics.tsv"
CREW    = "/home/abryant/database/title.crew.tsv"
VOTE_THRESHOLD = 5000
KEEP_THRESHOLD = 5000

# step 1 rating file to get views and ratings 

# create empty storage array
ratings = []

# parse ratings file
with open(RATINGS,"r") as ratings_fp:
    next(ratings_fp)
    for line in ratings_fp:

        # clean data for each line
        sub = (line.strip()).split('\t')
        title_id     = sub[0]
        title_rating = float(sub[1])
        title_votes  = float(sub[2])

        # append only if vote > 5000
        if title_votes > VOTE_THRESHOLD:
            ratings.append([title_id,title_rating,title_votes])

# no need to store this file pointer anymore
ratings_fp.close()

# step 2 create lists of most rated and viewed 

# store top 10000 by rating      
ratings.sort(reverse=True, key=lambda x:x[1])
top_rated = ratings[0:KEEP_THRESHOLD]

# store top 10000 by votes      
ratings.sort(reverse=True, key=lambda x:x[2])
top_voted = ratings[0:KEEP_THRESHOLD]

# step 3 merge the list

# combine lists
top_data = top_rated+top_voted

# make unique

# needed variables
uniq_data = []
prev_id = ""

# sort data by id 
top_data.sort(reverse=True, key=lambda x:x[0])

# go through entire array
for mp in top_data:

    # append if id doesnt match previous
    if mp[0] != prev_id:
        uniq_data.append(mp)

    # update comparator 
    prev_id = mp[0]

# step 4 get stuff from other files

# make empty array
basics = []

# parse ratings file
with open(BASICS,"r") as basics_fp:
    next(basics_fp) # skip header
    for line in basics_fp:

        # clean data for each line
        sub = (line.strip()).split('\t')

        # only keep movies 
        if (sub[1] == 'movie'):
                    
            # only keep action, drame, comedy
            genres = sub[8].split(",")
            for g in genres:
                if (g == 'Action') or (g == 'Comedy') or (g == 'Drama'):

                    # only append if it matches an id 
                    for mp in uniq_data:
                        if sub[0] == mp[0]:
                            basics.append(sub+[mp[1],mp[2]]) 
                            break 
# close pointer
basics_fp.close()

# make unique

# needed variables
output = ['tconst','titleType','primaryTitle','originalTitle','isAdult','startYear','endYear','runtimeMinutes','genres','averageRating','numVotes']
prev_id = ""

# sort data by id 
basics.sort(reverse=True, key=lambda x:x[0])

# go through entire array
for mp in basics:

    # append if id doesnt match previous
    if mp[0] != prev_id:
        output.append(mp)

    # update comparator 
    prev_id = mp[0]

# step 5 write to csv 
b = open('output.csv', 'w')
a = csv.writer(b)
a.writerows(output)
b.close()
