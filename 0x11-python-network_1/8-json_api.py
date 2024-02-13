#!/usr/bin/python3
"""
Takes a letter and sends a POST request to a URL"""
import requests
import requests.exceptions


def search(letter):
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})
    try:
        json_res = r.json()
        print(json_res)
        if len(json_res) < 1:
            return 'No result'
        else:
            return f'[{json_res.id}] {json_res.name}'
    except requests.exceptions.JSONDecodeError:
        return 'Not a valid JSON'


if __name__ == '__main__':
    import sys
    try:
        letter = sys.argv[1]
    except IndexError:
        letter = ""
    print(search(letter))
