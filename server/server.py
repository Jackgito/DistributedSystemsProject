import bcrypt # pip3 install bcrypt (used for password hashing)
import pymongo # pip3 install pymongo (MongoDB is database of choice)
from xmlrpc.server import SimpleXMLRPCServer

dbClient = pymongo.MongoClient("mongodb://localhost:27017/DSproject")  # DSproject is database name
db = dbClient["DSproject"]
collection = db["users"] # users is cluster name (cluster is like a table)

# Create a server instance
server = SimpleXMLRPCServer(("localhost", 3000))

# Start listening for requests
print("Server listening on port 3000")
server.serve_forever()


# Used for sign up
def is_username_unique(username):
  if collection.find_one({"username": username}):
    return True
  else:
    return False

def create_user(username, password):
  # Hash the password using bcrypt
  hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
  
  # Save username and hashed password to the database
  try:
    data = {"username": username, "password": hashed_password.decode('utf-8')}
    collection.insert_one(data)
  except:
    return False
  
  return True

def login(username, password):
    # Find user by username
    user = collection.find_one({"username": username})

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

def test():
   print("Test")
   return

server.register_function(test, "test")