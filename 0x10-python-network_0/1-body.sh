#!/bin/bash
# Send a GET request to the URL, and display the body of the response
curl -Ls -X "GET" --url "$1"
