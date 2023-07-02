#!/usr/bin/python3
"""This script fetches 'https://alx-intranet.hbtn.io/status'"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(
            "https://alx-intranet.hbtn.io/status") as response:
        print("Body response:$")
        print("\t- type: {}$".format(type(response.read())))
        print("\t- content: {}$".format(response.msg))
        print("\t- utf8 content: {}$".format(response.msg))
