from helper_functions import clear_screen
from authentication import show_authentication_menu
import xmlrpc.client # For communication with server
import show_posts
import create_post
import search_tweets_by_hashtag
import globals

# Connect to the server
SERVER_URL = "http://localhost:3000"
CLIENT = xmlrpc.client.ServerProxy(SERVER_URL)

def show_main_menu():
    while True:
      print("""
      What do you want to do?

      1. Show 10 latest posts
      2. Create a post
      3. Search posts by hashtag
      4. Sign out
      """)

      choice = input("Enter your choice: ")

      if choice == '1':
        #clear_screen()
        show_posts.show_posts(CLIENT)

      elif choice == '2':
        #clear_screen()
        create_post.create_post(CLIENT)
        
      elif choice == '3':
        #clear_screen()
        search_tweets_by_hashtag.search_tweets_by_hashtag(CLIENT)

      elif choice == '4':
        #clear_screen()
        globals.current_user = None
        return
      
      else:
        print("Invalid choice. Please try again.")

def main():

  while True:
      show_authentication_menu(CLIENT)
      show_main_menu()

if __name__ == "__main__":
  main()
