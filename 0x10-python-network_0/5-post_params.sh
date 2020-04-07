#!/bin/bash
# Takes in a URL, sends a POST request, and displays the body of the response
curl -X POST "$1" -d 'email=hr@holbertonschool.com&subject=I will always be here for PLD'
