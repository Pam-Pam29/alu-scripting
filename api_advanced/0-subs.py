#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of subscribers (all subscribers)
"""
import json  # Importing in alphabetical order
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    Args:
    subreddit (str): The subreddit to query.
    Returns:
    int: The number of subscribers if the subreddit is valid, 0 otherwise.
    """
    subreddit_URL = 'https://www.reddit.com/r/{}/about/.json'.format(subreddit)
    headers = {"user-agent": "user"}
    response = requests.get(subreddit_URL, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        subreddit_info = response.json()
        subscribers = subreddit_info.get("data", {}).get("subscribers")
        return subscribers if subscribers else 0
    else:
        return 0
