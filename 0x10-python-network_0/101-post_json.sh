#!/bin/bash
# Sends a JSON POST request to a URL, aand displays the body of the response
curl -s -X "POST" --data @"$2" --url "$1"
