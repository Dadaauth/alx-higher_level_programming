#!/usr/bin/python3
"""
sends a get request to a URL, if an http code greater
or equal to 400 is received, print 'Error code: <http_code>' """
import requests


def error_code(url):
    r = requests.get(url)
    if r.status_code >= 400:
        print(f'Error code: {r.status_code}')
    else:
        print(r.text)


if __name__ == '__main__':
    import sys
    url = sys.argv[1]
    error_code(url)
