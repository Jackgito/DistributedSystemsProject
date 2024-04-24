import requests # pip3 install requests 
from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime, timedelta

# Used for sign up. Returns true if username exits, false otherwise
def is_username_unique(username):

  url = 'http://localhost:5000/is_username_unique' 
  params = {"username": username}
  try: 
    response = requests.get(url, params=params) 
    data = response.json()

    return data['isUnique']
  except requests.exceptions as e:
    print(f"Request failed: {e}")
  return None

def go_through_posts(cursor):
  result_array=[]
  for post in cursor:
    result_array.append(post)
  for i in result_array:
    i['_id'] = str(i['_id']) # id and datetime needs to be converted to strings.
    i['Timestamp'] = str(i['Timestamp'])

    iso_date = datetime.fromisoformat(i['Timestamp'])+ timedelta(hours=3) # Formatting the date to wanted form +3 hours to match Helsinki timezone
    formatted_date = iso_date.strftime("%d/%m/%Y %H:%M")
    i['Timestamp'] = formatted_date 

  return result_array

def create_user(username, password): 

  # calling server to insert the user into the database
  data = {"username": username, "password": password}
  url = 'http://localhost:5000/create_user' 

  response = requests.post(url, json=data) 

  if (response.status_code == 201):
    return True
  else:
    return False

def login(username, password): 
    
  url = 'http://localhost:5000/login'
  data = {'username': username, 'password': password}
  response = requests.post(url, json=data)

  if response.status_code == 200:
    print("Login successful")
    return True
  elif response.status_code == 404:
    print("User not found")
    return False
  elif response.status_code == 401:
    print("Invalid credentials")
    return False
  else:
    print("Failed to authenticate")
    return False
    

def is_title_unique(title): 
  url = 'http://localhost:5000/is_title_unique' 
  params = {'title': title}

  response = requests.get(url, params=params)
  data = response.json()

  return data['isUnique']


def create_post(poster, title, postText, hashtags): 
  

  # Creates new post and adds it to database. Parameters:
  # - poster (str): the user who created the post
  # - title (str): title of the post
  # - postText (str): post content
  # - timestamp (datetime): time when post was created
  # - hashtags (list): list of hashtags associated with the post

  

  url = 'http://localhost:5000/create_post' 
  data = {"title": title, "poster": poster, "text": postText, "hashtags": hashtags}
  
  response = requests.post(url, json=data) 
  if (response.status_code == 201):
    return True
  else:
    return False
  

# Fetch 10 newest posts
def fetch_posts(): 
  # data = {"Title": "Title for post", "Poster": "username", "text":"Text for the post", "Timestamp":datetime.now(), "hashtags":["#hastag1", "#hastag2"], "Likes": 10, "Comments":["commenttext1"]}
  url = 'http://localhost:5000/posts' 
  response = requests.get(url) 
  
  if response.status_code == 200:
    posts = response.json() 
    return go_through_posts(posts)
  else:
    print("Error occurred when retrieving posts:", response.status_code)
    return None

# user may see only 50 newest posts
def fetch_own_posts(username):
  url = 'http://localhost:5000/ownPosts' 
  data = {'username': username}
  response = requests.post(url, json=data) 
  
  if response.status_code == 200:
    posts = response.json() 
    return go_through_posts(posts)

  else:
    print("Error occurred when retrieving own posts:", response.status_code)
    return None

def find_hashtag(hashtag): 
  url = 'http://localhost:5000/posts_hashtag' 
  params = {"hashtag": hashtag}
  response = requests.get(url, params=params) 
  
  if response.status_code == 200:
    posts = response.json() 
    return go_through_posts(posts)
  else:
    print("Error occurred when retrieving posts with hashtag:", response.status_code)
    return None

def like_post(post_name, username): 
  url = 'http://localhost:5000/like'
  data = {'title': post_name, 'username': username}
  response = requests.post(url, json=data)

  if response.status_code == 201:
    return "LikeAdded"
  elif response.status_code == 404:
    return "PostNotFound"
  elif response.status_code == 204:
    return "LikeRemoved"
  else:
    return "Error"
  
def comment_post(post_name, username, comment):
  url = 'http://localhost:5000/comment'
  data = {'title': post_name, 'username': username, 'comment': comment}
  response = requests.post(url, json=data)

  if response.status_code == 201:
    return "CommentAdded"
  elif response.status_code == 404:
    return "PostNotFound"
  else:
    return "Error"
  
def delete_post(post_name, username):
  url = "http://localhost:5000/delete"
  data = {'title': post_name, 'username': username}
  response = requests.delete(url, json=data)

  if response.status_code == 201:
    return "PostDeleted"
  elif response.status_code == 404:
    return "PostNotFound"
  else: 
    return "Error"

if __name__ == "__main__":
  PORT = 3000
  with SimpleXMLRPCServer(('localhost', PORT), allow_none=True) as server:
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
    server.register_function(delete_post)
    server.register_function(fetch_own_posts)

    print(f"Server running on port: {PORT}")
    print("Control-c to quit")

    try:
      server.serve_forever()
    except KeyboardInterrupt:
      exit(0)