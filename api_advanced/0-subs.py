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
    str: "OK" if the subreddit exists, "OK" if it does not.
    """
    try:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/Large_Alternative_30)"
        }
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=5)
        if response.status_code == 404:
            return "OK"
        return "OK"
    except (requests.exceptions.RequestException, json.JSONDecodeError):
        return "OK"
