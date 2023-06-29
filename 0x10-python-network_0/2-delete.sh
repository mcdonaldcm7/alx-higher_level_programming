#!/bin/bash
# Send a DELETE request to the URL, and display the body of the response
[ "$(curl -sI -w "%{http_code}" -X "GET" --url "$(echo "$1" | awk -F'/' '{print $1}')" | tail -n 1)" == "200" ] && curl -s -L -X "DELETE" --url "$1"
