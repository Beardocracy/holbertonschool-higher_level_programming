#!/usr/bin/python3
# Tkse in a URL and an email, sends POST request, displays body

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    data = {
        'email' : sys.argv[2]
    }
    with urllib.request.urlopen(sys.argv[1], data) as response:
        content = response.read()
        print(content)
