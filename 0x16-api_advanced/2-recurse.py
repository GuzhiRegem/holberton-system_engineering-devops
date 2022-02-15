#!/usr/bin/python3
"""
    module
"""
import requests


def recurse(subreddit, hot_list=[]):
    """ function """
    url = 'https://oauth.reddit.com/r/{}/new'.format(subreddit)
    if len(hot_list) > 0:
        url += "?after=t3_{}".format(
            hot_list[-1].get("data").get("id")
        )
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

    if response.status_code != 200:
        return []
    data = response.json().get("data")
    if data is None:
        return []
    if len(data.get("children")) == 0:
        return hot_list
    for post in data.get("children"):
        hot_list.append(post)
    return recurse(subreddit, hot_list)
