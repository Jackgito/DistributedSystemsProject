import bcrypt # pip3 install bcrypt (used for password hashing)
import pymongo # pip3 install pymongo (MongoDB is database of choice)
from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime
DBCLIENT = pymongo.MongoClient("mongodb://localhost:27017")
DBCLIENT.server_info()
print("Connection to MongoDB established successfully!")
DB = DBCLIENT["DSproject"]
COLLECTION = DB["users"] # users is cluster name (cluster is like a table)
POSTS = DB["Posts"]

# Used for sign up. Returns true if username exits, false otherwise
def is_username_unique(username):
  user_count = COLLECTION.count_documents({"username": username})
  return user_count == 0

def go_through_posts( cursor):
  result_array=[]
  for post in cursor:
    result_array.append(post)
  for i in result_array:
     i['_id'] = str(i['_id']) # id and datetime needs to be converted to strings.
     i['Timestamp'] = str(i['Timestamp'])
  return result_array

def create_user(username, password):
  # Hash the password using bcrypt
  hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
  
  # Save username and hashed password to the database
  try:
    data = {"username": username, "password": hashed_password.decode('utf-8')}
    COLLECTION.insert_one(data)
  except:
    return False
  
  return True

def login(username, password):
    # Find user by username
    user = COLLECTION.find_one({"username": username})

    # Check if username exists
    if user is None:
        print("Invalid username or password")
        return False

    # Verify password using bcrypt
    hashed_password = user["password"].encode('utf-8')  # Convert stored password to bytes

    if not bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        print("Invalid username or password")
        return False

    # Login successful
    print(f"Welcome back, {username}!")
    return True

def is_title_unique(title):
   if (POSTS.find_one({"Title": title})):
       return False
   
   return True

def create_post(poster, title, postText, timestamp, hashtags):
  '''
  Creates new post and adds it to database. Parameters:
  - poster (str): the user who created the post
  - title (str): title of the post
  - postText (str): post content
  - timestamp (datetime): time when post was created
  - hashtags (list): list of hashtags associated with the post
  '''
  try:
    data = {"Title": title, "Poster": poster, "text": postText, "Timestamp": timestamp, "hashtags": hashtags, "Likes": 0, "Comments": []}
    POSTS.insert_one(data)
  except:
    return False
  
  return True

# Fetch 10 newest posts
def fetch_posts():
  # data = {"Title": "Title for post", "Poster": "username", "text":"Text for the post", "Timestamp":datetime.now(), "hashtags":["#hastag1", "#hastag2"], "Likes": 10, "Comments":["commenttext1"]}
  # POSTS.insert_one(data)
  posts =POSTS.find().sort([('Timestamp', -1)]).limit(10)
  
  
  return go_through_posts(posts)

def find_hashtag(hashtag):
  posts = POSTS.find({"hashtags" : {"$in" : [hashtag]}})
  return go_through_posts(posts)

def like_post(post_name, username, comment):
  try:

    # Check if post exists
    if not POSTS.find_one({"Title": post_name}):
      return "PostNotFound"
    
    # Check if user has liked already. 
    # If they have, remove the like and user from the liked list
    if POSTS.find_one({"Title": post_name, "LikedUsers": {"$in": [username]}}):
      POSTS.find_one_and_update(
          {"Title": post_name, "LikedUsers": {"$in": [username]}},
          {"$pull": {"LikedUsers": username}, "$inc": {"Likes": -1}},
      )
      return "LikeRemoved"
    else:
      # User hasn't liked, so add like and user
      POSTS.find_one_and_update(
          {"Title": post_name},
          {"$inc": {"Likes": 1}, "$addToSet": {"LikedUsers": username}},
      )
      return "LikeAdded"

  except:
    return "Error"

def comment_post(post_name, username, comment):
  try:
    # Check if post exists
    if not POSTS.find_one({"Title": post_name}):
      return "PostNotFound"

    # Update the post with the new comment
    POSTS.find_one_and_update(
        {"Title": post_name},
        {"$push": {"Comments": {"Username": username, "Text": comment}}},
    )
    return "CommentAdded"

  except:
    return "Error"


if __name__ == "__main__":
    with SimpleXMLRPCServer(('localhost', 3000), allow_none=True) as server:
        server.register_introspection_functions()

        server.register_function(is_username_unique)
        server.register_function(create_user)
        server.register_function(fetch_posts)
        server.register_function(login)
        server.register_function(create_post)
        server.register_function(like_post)
        server.register_function(is_title_unique)
        server.register_function(find_hashtag)
        server.register_function(comment_post)

        print("Control-c to quit")

        try:
            server.serve_forever()
        except KeyboardInterrupt:
            exit(0)

