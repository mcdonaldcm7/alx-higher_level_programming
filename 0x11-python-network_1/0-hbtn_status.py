#!/usr/bin/python3
"""This script fetches 'https://alx-intranet.hbtn.io/status'"""
import urllib.request


with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    print("Body response:")
    print("\t- type: {}".format(type(response.read())))
    print("\t- content: {}".format(response.reason))
    print("\t- utf8 content: {}".format(response.msg))
