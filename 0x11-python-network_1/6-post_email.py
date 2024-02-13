#!/usr/bin/python3
"""
This script takes in a URL and an email address value.
It posts the email address value to the URL endpoint"""
import requests


def post_email(url, email):
    r = requests.post(url, data={'email': email})
    print(r.text)


if __name__ == '__main__':
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
