#!/bin/bash
# Send a GET request to the URL, and display the body of the response
host=$(echo "$1" | awk -F'/' '{print $1}')
code=$(curl -sI -w "%{http_code}" -X "GET" --url "$host" | tail -n 1)
if [ "$code"=="200" ]
then
        curl -L -X "GET" --url "$1"
fi
