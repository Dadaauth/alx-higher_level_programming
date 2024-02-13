#!/usr/bin/python3
"""takes in a GitHub credential and display an id using GitHub API"""
import requests


def github_api(username, password):
    url = f"https://api.github.com/users/{username}"
    r = requests.get(url, headers={
        "Authorization": f'Bearer {password}'
    })
    print(r.json().get('id'))


if __name__ == '__main__':
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    github_api(username, password)
