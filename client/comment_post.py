import globals

def comment_post(post_name, CLIENT):
  comment = input("Write your comment here: ")
  result = CLIENT.comment_post(post_name, globals.current_user, comment)
  
  if (result == "CommentAdded"):
    print("Comment added")
    return True
  
  if (result == "PostNotFound"):
    print("Post not found")
    return False
  
  if (result == "Error"):
    print("Error occurred")
    return False