#!/bin/bash
# Send a request to the URL provided and print the size of the response
curl -sI --url $1 | grep -i Content-Length | awk -F': ' '{print $2}'
