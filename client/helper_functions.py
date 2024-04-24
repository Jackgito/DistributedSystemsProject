import os

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def print_posts(array_of_posts):
  for post in array_of_posts:
    hashtags_formatted = ' '.join(f'#{tag}' for tag in post['hashtags'])
    comments_formatted = '\n'.join(f" {comment['Username']}: {comment['Text']}" for comment in post['Comments'])

    print(
        f''' 
        |{post['Poster']}: {post['Title']}| {post['Timestamp']}

        {post['text']}

        Likes: {post['Likes']} | Hashtags: {hashtags_formatted}
        ----------------------------
        Comments:
        {comments_formatted}
        '''
    )
  return