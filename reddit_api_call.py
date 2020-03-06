import requests
from post import RedditPost


class StatusCodeError:
    def __init__(self, code):
        self.code = code


def call(subreddit):
    collected_posts = []
    # Send a GET request to www.reddit.com with the sub-reddit in the URL
    search = requests.get('http://www.reddit.com/r/' + subreddit + '/.json',
                          headers={
                              'User-agent': 'Reddit Bot #^inf'
                          })
    if search.status_code != 200:
        raise StatusCodeError(search.status_code)
    # List of posts on this sub-reddit
    posts = search.json()['data']['children']
    for post in posts:
        collected_posts.append(RedditPost(post['data']))

    return collected_posts

