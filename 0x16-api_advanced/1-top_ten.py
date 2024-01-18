#!/usr/bin/python3
"""
Top 10 Subreddit posts
"""
import requests

def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Cassyeh-GitHub"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200 and not response.is_redirect:
            subreddit_data = response.json()
            for post in subreddit_data["data"]["children"]:
                print(post["data"]["title"])
        else:
            print("None")
    except Exception:
        print("None")
