#!/bin/bash
# Sends a request to a URL passed as an argument, and displays the status code of the response
curl -sI -w "%{http_code}" -X "GET" --url "$(echo "$1" | awk -F'/' '{print $1}')" | tail -n 1
