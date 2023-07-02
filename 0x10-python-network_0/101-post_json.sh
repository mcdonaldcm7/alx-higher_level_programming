#!/bin/bash
# Sends a JSON POST request to a URL, aand displays the body of the response
curl -s --header "Accept: application/json" --header "Content-Type: application/json" --data @"$2" --url "$1"
