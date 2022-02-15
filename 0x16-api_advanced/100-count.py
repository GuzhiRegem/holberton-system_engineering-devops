#!/usr/bin/python3
"""
    module
"""
import requests


def count_words(subreddit, word_list):
    """ function """
    if type(word_list) == list:
        lis = word_list[:]
        out = {
            "amounts": {},
            "lastone": None
        }
        for word in word_list:
            out["amounts"][word] = 0
        return count_words(subreddit, out)
    url = 'https://oauth.reddit.com/r/{}/hot'.format(subreddit)
    if word_list.get("lastone") is not None:
        url += "?after=t3_{}".format(
            word_list.get("lastone")
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
        return
    data = response.json().get("data")
    if data is None:
        return
    if len(data.get("children")) == 0:
        word_list["amounts"] = {k: v for k, v in sorted(
            word_list["amounts"].items(),
            key=lambda item: item[1],
            reverse=True
        )}
        for key, value in word_list.get("amounts").items():
            if value > 0:
                print("{}: {}".format(key, value))
        return
    for post in data.get("children"):
        words = post.get("data").get("title").lower()
        for word in word_list.get("amounts").keys():
            word_list["amounts"][word] += words.count(word)
    word_list["lastone"] = data.get("children")[-1].get("data").get("id")
    count_words(subreddit, word_list)
