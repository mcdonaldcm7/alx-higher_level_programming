#!/bin/bash
# Displays all HTTP methods the server will accept
curl -s -I $1 | grep -i Allow | awk -F': ' '{print $2}'
