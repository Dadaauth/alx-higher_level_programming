#!/usr/bin/python3
"""
Takes a letter and sends a POST request to a URL"""
import requests
import requests.exceptions


def search(letter):
    """My search function searching a Search API"""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})
    try:
        json_res = r.json()
        if len(json_res) < 1:
            return 'No result'
        else:
            return f'[{json_res.get('id')}] {json_res.get('name')}'
    except requests.exceptions.JSONDecodeError:
        return 'Not a valid JSON'


if __name__ == '__main__':
    import sys
    try:
        letter = sys.argv[1]
    except IndexError:
        letter = ""
    print(search(letter))
