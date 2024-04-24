from helper_functions import print_posts
import post_menu
import globals

def show_posts(CLIENT):
  arrayOfPosts=CLIENT.fetch_posts()
  print_posts(arrayOfPosts)
    
  # Like / comment on the posts
  while True:
    if (post_menu.post_menu(CLIENT) == False):
      break

# function to show only the users posts
def show_OWN_posts(CLIENT):
  arrayOfPosts=CLIENT.fetch_own_posts(globals.current_user)

  if (arrayOfPosts == None):
    print("No posts to show ARRAY NONE")
    return 0

  if ((len(arrayOfPosts) == 0)):
    print("No posts to show")
    return 0
  else: 
    print_posts(arrayOfPosts)

  # going back to the main menu
  return 0