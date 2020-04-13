#!/usr/bin/python3
# Takes a letter, send a POST request with the passed letter as parameter

import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        post_variable = {'q': sys.argv[1]}
    else:
        post_variable = {'q': ""}
    r = requests.post(url, data=post_variable)
    try:
        json_body = r.json()
        if json_body != {}:
            print("[{}] {}".format(json_body.get('id'), json_body.get('name')))
        else:
            print("No result")
    except ValueError:
        print('Not a valid JSON')
