from datetime import datetime

def create_post():
  post = input("What do you want to 'Tweet' about?: ") # Max 200 characters?
  timestamp = datetime.now()
  timestamp = timestamp.strftime("%m.%d.%Y")
  print("Post created")
  return