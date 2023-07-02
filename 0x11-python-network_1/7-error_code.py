#!/usr/bin/python3
"""
This script that takes in a URL, sends a request to the URL and displays the
body of the response
"""
import requests
import sys


if __name__ == "__main__":
    bad_r = requests.get(sys.argv[1])
    code = bar_r.status_code
    if code >= 400:
        print("Error code: {}".format(code))
