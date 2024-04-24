import globals
def delete_post(CLIENT):
    post_name = input("Write the name of the post to be deleted: ")

    result = CLIENT.delete_post(post_name, globals.current_user)

    if (result == "PostDeleted"):
        print("Post deleted")
        return True
  
    if (result == "PostNotFound"):
        print("Post not found")
        return False
    
    if (result == "Error"):
        print("Error occurred")
        return False
    else:
        print("Unknown response from server")
    return 0