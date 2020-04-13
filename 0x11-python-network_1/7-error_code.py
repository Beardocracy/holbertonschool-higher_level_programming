#!/usr/bin/python3
# Takes a URL, send a request, displays body or error code

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code == 200:
        print(r.text)
    else:
        print('Error code: {}'.format(r.status_code))
