import re
import globals 

def handle_signup(client) -> bool:
    username = input("Username: ")

    if len(username) == 0:
      print("Username is required")
      return False

    # Check if username exists already
    if client.is_username_unique(username) == False:
      print("Username already exists")
      return False

    # Check if password meets requirements
    print("Password must contain at least:\n  one lowercase letter")
    print("  one uppercase letter\n  one number\n  one special character.")
    password = input("Password: ")

    # Check if password is valid
    if not check_password(password):
        return False

    # Send the credentials to the server
    if not client.create_user(username, password):
        print("Sign up failed")
        return False

    globals.current_user = username
    print("Sign up successful")
    return True
        
def get_username_list():
   username_list = ["Juhani"]
   return username_list

def handle_login(client):
    username = input("Username: ")
    password = input("Password: ")
    
    if(not client.login(username, password)):
       print("Invalid credentials")
       return False
      
    globals.current_user = username
    print("Login successful")
    return True


def show_authentication_menu(client):
    while True:
      print("""
      Welcome to "Twitter"

      1. Sign Up
      2. Login

      0. Exit
      """)

      choice = input("Enter your choice: ")

      if choice == '1':
        if handle_signup(client):
          return
      elif choice == '2':
        if handle_login(client):
          return
      elif choice == '0':
        quit()
      else:
        print("Invalid choice. Please try again.")


def check_password(password):
  # Checks password complexity and returns True if valid, False otherwise.
  # Requirements:
  # - Minimum length of 8 characters
  # - Contains at least one lowercase letter
  # - Contains at least one uppercase letter
  # - Contains at least one number (0-9)
  # - Contains at least one special character (!@#$%^&*()_+-=[]{};':|\,.<>/?)

  # Minimum length check
  if len(password) < 8:
    print("Password must be at least 8 characters long.")
    return False

  # Character type checks using regular expressions
  has_lower = bool(re.search(r"[a-z]", password))
  has_upper = bool(re.search(r"[A-Z]", password))
  has_digit = bool(re.search(r"[0-9]", password))
  #has_special = bool(re.search(r"[!@#$%^&*()_+-={}[\];':|\,.<>/?]", password))

  has_special = False
  special = "!@#$€£§%^&*()_+-={}[];\"':|\\,.<>/?"

  for c in password:
      if c in special:
          has_special = True
          break

  # Check for all character types
  valid = has_lower and has_upper and has_digit and has_special

  if not valid:
      print("Password does not match requirements")

  return valid
