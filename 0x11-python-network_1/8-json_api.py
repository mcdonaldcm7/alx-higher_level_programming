#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request  to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    param = sys.argv[1] if len(sys.argv) == 2 else ""
    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": param})
    try:
        res = r.json()
        if len(res) == 0:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except requests.exceptions.JSONDecodeError as e:
        print("Not a valid JSON")
