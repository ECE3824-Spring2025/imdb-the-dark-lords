import movie_data

# Deduplicate and sort by rating for the "rating" lists:
ListWithRatingDrama_NoRepeats = {m['id']: m for m in movie_data.ListWithRatingDrama}.values()
sorted_ListWithRatingDrama_NoRepeats = sorted(ListWithRatingDrama_NoRepeats, key=lambda x: x['rating'], reverse=True)

ListWithRatingAction_NoRepeats = {m['id']: m for m in movie_data.ListWithRatingAction}.values()
sorted_ListWithRatingAction_NoRepeats = sorted(ListWithRatingAction_NoRepeats, key=lambda x: x['rating'], reverse=True)

ListWithRatingComedy_NoRepeats = {m['id']: m for m in movie_data.ListWithRatingComedy}.values()
sorted_ListWithRatingComedy_NoRepeats = sorted(ListWithRatingComedy_NoRepeats, key=lambda x: x['rating'], reverse=True)

# Deduplicate and sort by votes for the "likes" lists:
ListWithLikesDrama_NoRepeats = {m['id']: m for m in movie_data.ListWithLikesDrama}.values()
sorted_ListWithLikesDrama_NoRepeats = sorted(ListWithLikesDrama_NoRepeats, key=lambda x: x['votes'], reverse=True)

ListWithLikesAction_NoRepeats = {m['id']: m for m in movie_data.ListWithLikesAction}.values()
sorted_ListWithLikesAction_NoRepeats = sorted(ListWithLikesAction_NoRepeats, key=lambda x: x['votes'], reverse=True)

ListWithLikesComedy_NoRepeats = {m['id']: m for m in movie_data.ListWithLikesComedy}.values()
sorted_ListWithLikesComedy_NoRepeats = sorted(ListWithLikesComedy_NoRepeats, key=lambda x: x['votes'], reverse=True)