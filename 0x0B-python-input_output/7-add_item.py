#!/usr/bin/python3
"""
This script adds all arguments to a Python list, and then save them to a file.
It uses the 'save_to_json_file' and 'load_from_json_file' functions to
accomplish this
"""


import json
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
obj = []

if os.path.isfile(filename):
    obj = load_from_json_file(filename)
for arg in sys.argv[1:]:
    obj.append(arg)
save_to_json_file(obj, filename)
