#!/usr/bin/python3
"""
    module
"""
import json
import requests
import sys

if __name__ == "__main__":
    num = sys.argv[1]
    request_raw = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            num))
    user_raw = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
            num))
    username = json.loads(user_raw.text).get("username")
    request_list = json.loads(request_raw.text)
    tasks = []
    for a in request_list:
        tasks.append(
            {
                "task": a.get("title"),
                "completed": a.get("completed"),
                "username": username
            }
        )
    out = {"{}".format(num): tasks}
    with open('{}.json'.format(num), 'w') as f:
        f.write(json.dumps(out))
