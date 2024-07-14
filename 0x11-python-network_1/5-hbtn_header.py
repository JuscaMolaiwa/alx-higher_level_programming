#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the
response using requests
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    Takes in a URL, sends a request to the URL and displays
    the value of the X-Request-Id variable found in the header
    of the response using requests
    """
    if len(argv) != 2:
        print("Usage: ./5-hbtn_header.py <URL>")
        exit(1)

    url = argv[1]
    try:
        r = requests.get(url)
        r_id = r.headers['X-Request-Id']
        print(r_id)
