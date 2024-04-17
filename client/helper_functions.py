import os

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def print_posts(array_of_posts):
  for post in array_of_posts:
    hashtags_formatted = ' '.join(f'#{tag}' for tag in post['hashtags'])
    print(
        f''' 
      |{post['Poster']}: {post['Title']}| {post['Timestamp']}

      {post['text']}

      Likes: {post['Likes']} | Hashtags: {hashtags_formatted}
        ----------------------------
      Comments:
        {post['Comments']}
        ''')
