#!/usr/bin/python3
"""
Queries the Reddit API and prints the number of subscribers for a given subreddit.
"""

import sys


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        number_of_subscribers = __import__('0-subs').number_of_subscribers
        if number_of_subscribers(sys.argv[1]) > 0:
            print("OK")
        else:
            print("Not a valid subreddit")
