#!/usr/bin/python3
"""
    module
"""
import requests


def top_ten(subreddit):
    """ function """
    url = 'https://oauth.reddit.com/r/{}/hot?limit=10'.format(subreddit)
    CLIENT_ID = "HS53oPaWudvShOpWbllhWw"
    SECRET_ID = "WvKok6fZNsaeE4jfTzGFs-PkvOs1BA"

    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_ID)
    token = requests.post(
        'https://www.reddit.com/api/v1/access_token',
        auth=auth,
        data={'grant_type': 'client_credentials'},
        headers={'user-Agent': 'hbtn'}
    ).json()['access_token']
    response = requests.get(
        url,
        headers={
            'user-Agent': 'hbtn',
            'Authorization': 'bearer {}'.format(token)
            },
        allow_redirects=False
    )

    data = response.json().get("data")
    if data is None:
        print(None)
    else:
        for post in data.get("children"):
            print(post.get("data").get("title"))
