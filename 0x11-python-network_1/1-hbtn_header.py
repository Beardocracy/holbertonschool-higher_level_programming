#!/usr/bin/python3
# Takes in a URL, send a request, and displays the value of the X-request-Id

import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        content = response.info()
        print(content.get('X-Request-Id'))
