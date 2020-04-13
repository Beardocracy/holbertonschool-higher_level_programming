#!/usr/bin/python3
# Takes a URL and email address, send a POST request with the passed email

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    post_variable = {'email': sys.argv[2]}
    r = requests.post(url, data=post_variable)
    print(r.text)
