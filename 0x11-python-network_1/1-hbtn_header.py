#!/usr/bin/python3
"""
Sends a request to the URL passed as a command line argument and displays
the value of the X-Request-Id variable found in the header of the response
"""
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.getheader("X-Request-Id"))
