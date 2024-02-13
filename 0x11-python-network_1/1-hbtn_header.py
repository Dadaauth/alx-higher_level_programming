#!/usr/bin/python3
"""
My module documentation. A docstring"""

import urllib.request


def fetch_header(url):
    with urllib.request.urlopen(url) as response:
        print(response.info().get('X-Request-Id'))


if __name__ == '__main__':
    import sys
    url = sys.argv[1]
    fetch_header(url)
