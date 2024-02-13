#!/usr/bin/python3
"""
My module is well documented
We start to use the requests module in this file"""
import requests


def get_status():
    r = requests.get('https://alx-intranet.hbtn.io/status')
    report = f"Body response:\n\t- type: {type(r.text)}\n\t" \
             f"- content: {r.text}"
    print(report)


if __name__ == '__main__':
    get_status()
