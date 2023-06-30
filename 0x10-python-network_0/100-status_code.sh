#!/bin/bash
# Sends a request to a URL passed as an argument, and displays the status code of the response
curl -s -o /dev/null -w "%{http_code}\n" --url "$1"
