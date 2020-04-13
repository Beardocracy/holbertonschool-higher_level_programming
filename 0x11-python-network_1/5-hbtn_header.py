#!/usr/bin/python3
# Takes a URL, displays the value of a variable

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    header_variable = 'X-Request-Id'
    r = requests.get(url)
    print(r.headers.get(header_variable))
