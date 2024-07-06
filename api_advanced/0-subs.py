#!/usr/bin/python3
"""
0-subs
"""
import json
import requests

def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit.
    
    Args:
    subreddit (str): The subreddit to query.
    
    Returns:
    int: The total number of subscribers. 0 if the subreddit is invalid.
    """
    try:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/Large_Alternative_30)"
        }
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=5)
        if response.status_code == 404:
            return 0
        results = response.json().get("data")
        return results.get("subscribers")
    except (requests.exceptions.RequestException, json.JSONDecodeError):
        return 0
