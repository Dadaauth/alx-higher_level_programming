#!/usr/bin/python3
"""
Secodn script to write using the requests module"""
import requests
import sys


def get_header(url):
    r = requests.get(url)
    return r.headers.get('X-Request-Id')


if __name__ == '__main__':
    url = sys.argv[1]
    print(get_header(url))
