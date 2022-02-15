#!/usr/bin/python3
"""
    module
"""
import requests


def number_of_subscribers(subreddit):
    """ function """
    url = 'https://oauth.reddit.com/r/{}/about'.format(subreddit)
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
            }
    )

    try:
        out = response.json()
        return out["data"]["subscribers"]
    except Exception:
        return 0
