from datetime import datetime
import globals

def create_post(CLIENT):
  poster = globals.current_user
  title = ""
  post = ""
  hashtags = []
  timestamp = datetime.now()
  timestamp = timestamp.strftime("%m.%d.%Y")

  while not title:
    title = input("Give a title for your Tweet: ")
    if not title: 
      print("Please enter a title for your Tweet")

  while not post:
    post = input("What do you want to 'Tweet' about? (Max 200 characters): ") 
    if not post: 
      print("Please enter content for your Tweet")
    elif len(post) > 200: 
      print("Your tweet can't exceed 200 characters.")
      post = ""

  if (input("Add hashtags for your Tweet? (y/n) ") == "y"):
    hashtags = input("Enter hashtags (separate with space): ").split(" ")

  if (CLIENT.create_post(poster, title, post, timestamp, hashtags)):
    print("Post created")
  else: 
    print("Post could not be created")

  return