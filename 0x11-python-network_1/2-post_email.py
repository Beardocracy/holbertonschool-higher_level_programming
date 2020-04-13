#!/usr/bin/python3
# Tkse in a URL and an email, sends POST request, displays body

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    values = {
        'email' : sys.argv[2]
    }
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print(content.decode('utf-8'))
