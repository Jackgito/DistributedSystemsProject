

def check_password(password):
  """
  Checks password complexity and returns True if valid, False otherwise.

  Requirements:
  - Minimum length of 8 characters
  - Contains at least one lowercase letter
  - Contains at least one uppercase letter
  - Contains at least one number (0-9)
  - Contains at least one special character (!@#$%^&*()_+-=[]{};':|\,.<>/?)
  """
  # Minimum length check
  if len(password) < 8:
    print("Password must be at least 8 characters long.")
    return False

  # Character type checks using regular expressions
  import re
  has_lower = bool(re.search(r"[a-z]", password))
  has_upper = bool(re.search(r"[A-Z]", password))
  has_digit = bool(re.search(r"\d", password))
  has_special = bool(re.search(r"[!@#$%^&*()_+-=[]{};':|\,.<>/?]", password))

  # Check for all character types
  if not (has_lower and has_upper and has_digit and has_special):
    return False

  # Password is valid
  return True

def handle_signup():
  while True:
    username = input("Username: ")
    # Check if username exists already
    if username!=username:
      print("username already exists")
      continue

    # Check if password meets requirements
    print("Password must contain at least one lowercase letter, one uppercase letter, one number, and one special character.")
    password = input("Password: ")

    if check_password(password):
      return

    # try:
    #   sign_up()
    # except:
    #   print("Authentication failed")

    return

def handle_login():
  username = input("Username: ")
  password = input("Password: ")

  # try:
  #   authenticate()
  # except:
  #   print("Authentication failed")

  return

def show_authentication_menu():
    print("""
    Welcome to "Twitter"

    1. Sign Up
    2. Login

    0. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == '1':
      handle_signup()
    elif choice == '2':
      handle_login()
    elif choice == '0':
      quit()
    else:
      print("Invalid choice. Please try again.")
    
    return