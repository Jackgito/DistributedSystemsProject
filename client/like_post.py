import globals

def like_post(post_name, CLIENT):
    result = CLIENT.like_post(post_name, globals.current_user)
    
    if (result == "LikeAdded"):
      print("Like added")
      return True

    if (result == "LikeRemoved"):
      print("Like removed")
      return True
    
    if (result == "PostNotFound"):
      print("Post not found")
      return False
    
    if (result == "Error"):
      print("Error occurred")
      return False