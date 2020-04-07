#!/bin/bash
# Takes in a URL, sends a request, displays all HTTP methods the server accepts
curl -sI "$1" | sed -n '/Allow/ s/Allow: //p'
