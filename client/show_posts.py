from helper_functions import print_posts
import post_menu

def show_posts(CLIENT):
    arrayOfPosts=CLIENT.fetch_posts()
    print_posts(arrayOfPosts)
      
    # Like / comment on the posts
    if (len(arrayOfPosts)==0):
       print("No posts to show!")
       return
    while True:
      if (post_menu.post_menu(CLIENT) == False):
         break
      