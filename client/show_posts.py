
def printPost(post):
    hashtags_formatted = ' '.join(f'#{tag}' for tag in post['hashtags'])
    print(
        f''' 
       |{post['Poster']}: {post['Title']}|

        {post['text']}

        Likes: {post['Likes']} | Hashtags {hashtags_formatted}
        ----------------------------
        Comments:
        {post['Comments']}
        ''')


def show_posts(client):
    arrayOfPosts=client.fetchPosts()
    for i in arrayOfPosts:
        printPost(i)
    return 