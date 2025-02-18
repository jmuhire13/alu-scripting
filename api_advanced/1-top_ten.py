#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
of a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Fetches and prints the first 10 hot post titles of a subreddit.
    If the subreddit is invalid, prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (compatible; ALU-Scripting/1.0)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts[:10]:
            print(post["data"]["title"])

    except Exception:
        print(None)

