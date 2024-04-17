from helper_functions import print_posts
def search_tweets_by_hashtag(CLIENT):
  hashtag = input("Search with hastag : #")
  found_posts = CLIENT.find_hashtag(hashtag)
  if len(found_posts) != 0:
    print_posts(found_posts)
  else:
    print("Ther was no found posts with this hashtag")
  return