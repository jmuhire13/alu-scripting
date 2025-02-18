#!/usr/bin/python3
"""API"""
import requests


def top_ten(subreddit):
    """Fetch and print the top 10 hot posts from a subreddit."""
    reddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(reddit_url, headers=headers, params={'limit': 10})

    # Check if the subreddit exists and the request was successful
    if response.status_code == 200:
        data = response.json().get('data', {})
        posts = data.get('children', [])
        if posts:
            for post in posts:
                print(post['data']['title'])
        else:
            print("OK")  # Subreddit exists but has no posts
    else:
        print("OK")  # Subreddit does not exist or other error
