import like_post
import comment_post

def post_menu(CLIENT):
  print("""
  What do you want to do?
  1. Like a post
  2. Comment a post
  3. Return to main menu
  """)

  choice = input("Enter your choice: ")

  if choice == '1':
    post_name = input("Enter name of the post: ")
    like_post.like_post(post_name, CLIENT)
    
  elif choice == '2':
    post_name = input("Enter name of the post: ")
    comment_post.comment_post(post_name, CLIENT)

  elif choice == '3':
    return False

  else:
    print("Invalid choice. Please try again.")

  return True