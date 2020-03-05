import requests
from post import RedditPost


def call(subreddit):
    collected_posts = []
    # Send a GET request to www.reddit.com with the sub-reddit in the URL
    search = requests.get('http://www.reddit.com/r/' + subreddit + '/.json',
                          headers={
                              'User-agent': 'Reddit Bot #^inf'
                          })
    # List of posts on this sub-reddit
    posts = search.json()['data']['children']
    for post in posts:
        collected_posts.append(RedditPost(post['data']))
        print("----------------------------------------------------------------------------")
        print(collected_posts[len(collected_posts) - 1])

    return collected_posts

