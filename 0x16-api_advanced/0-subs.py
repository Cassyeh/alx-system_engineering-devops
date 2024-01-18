#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Cassyeh-GitHub"}
    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            subreddit_data = response.json()
            return subreddit_data["data"]["subscribers"]

        else:
            return 0

    except Exception:
        return 0
