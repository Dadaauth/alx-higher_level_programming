#!/usr/bin/python3
"""
A module to work on in this alxswe project"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intran'
                                'et.hbtn.io/status') as response:
        res = {
            'data': response.read()
        }
        print(f"Body response:\n\t- type: {type(res.get('data'))}\n\t"
              f"- content: {res.get('data')}\n\t"
              f"- utf8 content: {res.get('data').decode('utf8')}")
