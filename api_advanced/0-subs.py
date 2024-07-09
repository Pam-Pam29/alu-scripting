#!/usr/bin/python3
"""A function that queries the Reddit API and
 returns the number of subscribers (all subscribers)"""


def number_of_subscribers(subreddit):
    """
    queries the Reddit API
    returns the number of subscribers for a given reddit
    """
    import json
    import requests
    subreddit_URL = 'https://www.reddit.com/r/{}/about/.json'.format(
        subreddit)
    response = requests.get(subreddit_URL,
                            headers={"user-agent": "user"},
                            allow_redirects=False)
    if response.status_code == 200:
        subreddit_info = response.json()
        if "data" not in subreddit_info:
            return 0
        subscribers = subreddit_info.get("data").get("subscribers")
        return subscribers
    else:
        return 0
