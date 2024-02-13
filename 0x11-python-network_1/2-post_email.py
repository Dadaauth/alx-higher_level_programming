#!/usr/bin/python3
"""
sends a POST request to a passed URL with a parameter"""
import urllib
import sys


def post_email(url, email):
    data = {
        'email': email
    }
    data = urllib.parse.urlencode(data)
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        res = response.read()
        print(res.decode('utf8'))


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
