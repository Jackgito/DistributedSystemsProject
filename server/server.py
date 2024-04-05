import bcrypt # pip3 install bcrypt (used for password hashing)
import pymongo # pip3 install pymongo (MongoDB is database of choice)
from xmlrpc.server import SimpleXMLRPCServer

DBCLIENT = pymongo.MongoClient("mongodb://localhost:27017")
DB = DBCLIENT["DSproject"]
COLLECTION = DB["users"] # users is cluster name (cluster is like a table)

# Used for sign up
def is_username_unique(username):
  return COLLECTION.find_one({"username": username})

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

if __name__ == "__main__":
    with SimpleXMLRPCServer(('localhost', 3000), allow_none=True) as server:
        server.register_introspection_functions()

        server.register_function(is_username_unique)
        server.register_function(create_user)

        print("Control-c to quit")

        try:
            server.serve_forever()
        except KeyboardInterrupt:
            exit(0)

