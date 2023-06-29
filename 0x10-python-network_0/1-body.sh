#!/bin/bash
# Send a GET request to the URL, and display the body of the response
code=$(curl -sI -w "%{http_code}" -X "GET" --url "$1" | tail -n 1)
if [ "$code"=="302" ]
then
        curl -L -X "GET" --url "$1"
fi
