#!/bin/bash
# Takes in a URL, sends a request, displays size of the body
curl -sI "$1" | sed -n '/Content-Length/ s/Content-Length: //p'
