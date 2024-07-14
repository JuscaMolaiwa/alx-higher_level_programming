#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL, and displays the
value of the X-Request-Id variable found in the header of the
response using requests.
"""

import requests
from sys import argv


if __name__ == "__main__":
    """Takes in a URL, sends a request to the URL, and displays
    the value of the X-Request-Id variable found in the header
    of the response using requests."""
    try:
        url = argv[1]
        r = requests.get(url)
        r.raise_for_status()  # Raise an exception for bad response status

        r_id = r.headers.get('X-Request-Id')
        if r_id:
            print(r_id)
        else:
            print("No X-Request-Id found in the response headers.")
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
