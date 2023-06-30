#!/bin/bash
# Send a GET request to the URL, and display the body of the response
[ "$(curl -s -o /dev/null -w "%{http_code}" --url "$1")" == "200" ] && curl -s -L -X "GET" --url "$1"
