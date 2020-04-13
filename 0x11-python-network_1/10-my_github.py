#!/usr/bin/python3
# Takes your github credentials and displays your ID

import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    print(r.json().get('id'))
