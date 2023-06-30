#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")
    req = urllib.request.Request(sys.argv[1], sys.argv[2])
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"), end="")
