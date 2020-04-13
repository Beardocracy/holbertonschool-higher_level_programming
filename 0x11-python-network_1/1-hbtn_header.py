#!/usr/bin/python3
# Takes in a URL, send a request, and displays the value of the X-request-Id

import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as response:
    content = dict(response.info())
    print(content.get('X-Request-Id'))
