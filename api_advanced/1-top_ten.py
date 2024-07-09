#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

Imports:
    json: for handling JSON data
    requests: for making HTTP requests to the Reddit API

Functions:
    top_ten(subreddit): queries the Reddit API and prints the titles of the first 10 hot posts for the given subreddit
"""

import json
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for the given subreddit.

    Args:
        subreddit (str): the subreddit to query

    Returns:
        None
    """
    subreddit_URL = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    response = requests.get(subreddit_URL, headers={"user-agent": "user"}, allow_redirects=False)
    if response.status_code == 200:
        subreddit_info = response.json()
        if "data" not in subreddit_info:
            print("None")
            return
        children = subreddit_info.get("data").get("children")
        for child in children:
            print(child.get("data").get("title"))
    else:
        print("None")
