#!/usr/bin/python3
"""
My module is well documented"""
import urllib.request
import urllib.error
import sys


def error_code(url):
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf8')
    except urllib.error.HTTPError as e:
        return f"Error code: {e.code}"


if __name__ == '__main__':
    url = sys.argv[1]
    print(error_code(url))