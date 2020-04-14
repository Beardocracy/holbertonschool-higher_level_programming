#!/usr/bin/python3
# Takes a repo name and owner name, lists the last 10 commits by owner

import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2],
                                                              sys.argv[1])
    r = requests.get(url)
    com_list = r.json()
    com_dict = {}
    for coms in com_list:
        date = coms.get('commit').get('author').get('date')
        sha = coms.get('sha')
        name = coms.get('commit').get('author').get('name')
        com_dict.update({date: {'sha': sha, 'name': name}})
    i = 0
    for k in sorted(com_dict.keys(), reverse=True):
        if i < 10:
            print("{}: {}".format(com_dict.get(k).get('sha'),
                                  com_dict.get(k).get('name')))
        i += 1
