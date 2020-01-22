#!/usr/bin/python3
import sys
import json


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    my_list = load_from_json_file('add_item.json')
except:
    my_list = []

i = 0
for items in sys.argv:
    if i > 0:
        my_list.append(items)
    i += 1

save_to_json_file(my_list, 'add_item.json')
