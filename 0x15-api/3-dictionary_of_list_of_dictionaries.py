#!/usr/bin/python3
"""
    module
"""
import requests
import json


def get_users_task(userid, username):
    request_raw = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            userid))
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
    return tasks


if __name__ == "__main__":
    user_raw = requests.get(
        'https://jsonplaceholder.typicode.com/users')
    user_list = json.loads(user_raw.text)
    out = {}
    for user in user_list:
        data = get_users_task(user.get("id"), user.get("name"))
        out["{}".format(user.get("id"))] = data
    with open('todo_all_employees.json', 'w', newline='') as f:
        f.write(json.dumps(out))
