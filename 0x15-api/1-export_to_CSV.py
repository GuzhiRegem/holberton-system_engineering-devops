#!/usr/bin/python3
"""
    module
"""
import re
import requests
import sys
import json
import csv

if __name__ == "__main__":
    num = sys.argv[1]
    request_raw = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            num))
    user_raw = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
            num))
    username = json.loads(user_raw.text).get("name")
    request_list = json.loads(request_raw.text)
    with open('{}.csv'.format(num), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for req in request_list:
            writer.writerow([str(num), username, req.get("completed"), req.get("title")])