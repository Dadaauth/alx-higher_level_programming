#!/usr/bin/python3
"""ALXSWE Interview preparation task"""
import requests
import sys


def get_commits(repo, user):
    url = f"https://api.github.com/repos/{user}/{repo}/commits"
    r = requests.get(url)
    json_r = r.json()
    count = 0
    for json_res in json_r:
        if count == 10:
            break
        else:
            count += 1
        print(f"{json_res.get('sha')}: "
              f"{json_res.get('commit').get('author').get('name')}")


if __name__ == '__main__':
    repo = sys.argv[1]
    user = sys.argv[2]
    get_commits(repo, user)
