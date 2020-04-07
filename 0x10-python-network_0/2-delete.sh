#!/bin/bash
# Takes in a URL, send a DELETE request, displays body of response
curl -s -X DELETE "$1"
