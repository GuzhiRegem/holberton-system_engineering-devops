#!/usr/bin/python3
"""
    module
"""
import json
import requests
import sys

if __name__ == "__main__":
    request_raw = requests.get(
        'https://jsonplaceholder.typicode.com/todos')
    user_raw = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
            sys.argv[1]))
    username = json.loads(user_raw.text).get("name")
    request_list = json.loads(request_raw.text)
    finished = []
    count = 0
    for a in request_list:
        if str(a.get("userId")) == sys.argv[1]:
            if a.get("completed"):
                finished.append(a.get("title"))
            count += 1
    print("Employee {} is done with tasks({}/{}):".format(
        username,
        len(finished),
        count
    ))
    for a in finished:
        print("    ", a)
