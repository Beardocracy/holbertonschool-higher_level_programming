#!/bin/bash
# Takes in a URL, sends a request, displays size of the body

if [[ $# -lt 1 ]]; then
    echo "Usage: 0-body_size.sh URL"
    exit
fi
curl -sI "$1" | sed -n '/Content-Length/ s/Content-Length: //p'
