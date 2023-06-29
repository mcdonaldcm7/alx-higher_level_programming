#!/bin/bash
# Send a GET request to the URL, and display the body of the response
[ "$(curl -sI -w "%{http_code}" -X "GET" --url "$(echo "$1" | awk -F'/' '{print $1}')" | tail -n 1)" == "200" ] && curl -L -X "GET" --url "$1"
