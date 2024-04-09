
def printPost(post):
    
    print(
        f''' 
       |{post['Poster']}: {post['Title']}|

        {post['text']}

        Likes: {post['Likes']} | Hashtags # {post['hashtags']}
        ----------------------------
        Comments:
        {post['Comments']}
        ''')


def show_posts(client):
    arrayOfPosts=client.fetchPosts()
    for i in arrayOfPosts:
        printPost(i)
    return 