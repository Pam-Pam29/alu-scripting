#!/usr/bin/python3
"""
0-main
"""
import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Usage: python 0-main.py <subreddit>")
        print("Example: python 0-main.py python")
    else:
        try:
            result = number_of_subscribers(sys.argv[1])
            if result > 0:
                print("OK")
            else:
                print("Not a subreddit")
        except Exception as e:
            print("Error: {}".format(e))
