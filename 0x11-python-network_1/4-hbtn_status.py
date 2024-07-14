#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using requests and displays the response information.
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    r = requests.get(url)
    content_type = type(r.text).__name__

    print("Body response:")
    print("\t- type: {}".format(content_type))
    print("\t- content: {}".format(r.text))
