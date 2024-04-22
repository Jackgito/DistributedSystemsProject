from helper_functions import print_posts
import post_menu

def search_tweets_by_hashtag(CLIENT):
  hashtag = input("Search with hastag : #")
  found_posts = CLIENT.find_hashtag(hashtag)
  if len(found_posts) != 0:
    print_posts(found_posts)

    # Like / comment on the posts
    while True:
      if (post_menu.post_menu(CLIENT) == False):
         break
  else:
    print("No posts found with this hashtag")
  return