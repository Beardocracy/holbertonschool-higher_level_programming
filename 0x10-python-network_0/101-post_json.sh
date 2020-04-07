#!/bin/bash
# Send a JSON POST request to a URL passed as an argument
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
