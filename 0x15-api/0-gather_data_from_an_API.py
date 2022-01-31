#!/usr/bin/python3
"""
    module
"""
import json
import requests
import sys

if __name__ == "__main__":
    username = json.loads(
        requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(
                sys.argv[1])).text).get("name")
    req_list = json.loads(
        requests.get(
            "https://jsonplaceholder.typicode.com/todos/" +
            "?userId=" + sys.argv[1]).text)
    com = [req.get("title") for req in req_list if req.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        username, len(com), len(req_list)), *com, sep="\n\t ")
