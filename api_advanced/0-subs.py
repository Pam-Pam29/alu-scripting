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
    subreddit_info = requests.get(subreddit_URL, headers=headers, allow_redirects=False).json()
    
    if "data" not in subreddit_info:
        return 0
    subscribers = subreddit_info.get("data", {}).get("subscribers")
    return subscribers if subscribers else 0
