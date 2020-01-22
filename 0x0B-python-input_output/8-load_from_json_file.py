#!/usr/bin/python3


import json


def load_from_json_file(filename):
    with open(filename, 'r') as f:
        object_from_json = json.loads(f.read())
    return object_from_json
