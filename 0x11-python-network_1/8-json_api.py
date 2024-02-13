#!/usr/bin/python3
"""Takes a letter and sends a POST request to a URL."""

import requests
import sys


def search(letter):
    """My search function searching a Search API"""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})
    try:
        """here is a documentation"""
        json_res = r.json()
        if len(json_res) < 1:
            return 'No result'
        else:
            return f"[{json_res.get('id')}] {json_res.get('name')}"
    except requests.exceptions.RequestException as e:
        """here is a documentation"""
        return 'Not a valid JSON'


if __name__ == '__main__':
    try:
        """here is a documentation"""
        letter = sys.argv[1]
    except IndexError:
        """here is a documentation"""
        letter = ""
    print(search(letter))
