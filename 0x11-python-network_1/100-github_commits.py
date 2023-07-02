#!/usr/bin/python3
"""
This script prints 10 commits (from the most recent to oldest) of the
repository \"rails\" by the user \"rails\"
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1]
            )
    r = requests.get(url=url)
    res = r.json()
    count = 0
    for key in res:
        print("{}: {}".format(
            key.get("sha"),
            key.get("commit").get("author").get("name")))
        count += 1
        if (count >= 10):
            break
