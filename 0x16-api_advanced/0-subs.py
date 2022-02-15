#!/usr/bin/python3
"""
    module
"""
import requests
import json


def number_of_subscribers(subreddit):
    """ function """
    CLIENT_ID = "HS53oPaWudvShOpWbllhWw"
    SECRET_ID = "WvKok6fZNsaeE4jfTzGFs-PkvOs1BA"
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_ID)
    data = {
        'grant_type': 'password',
        'username': 'Guzhi',
        'password': 'chino loco 1'
    }
    headers = {'User-Agent': 'MyBot/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
    response = requests.get(
        'https://oauth.reddit.com/r/{}/about'.format(subreddit),
        headers=headers
    )
    try:
        out = json.loads(response.text)
        return out["data"]["subscribers"]
    except Exception:
        return 0
