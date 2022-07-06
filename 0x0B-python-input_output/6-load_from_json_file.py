#!/usr/bin/python3
"""creates objects from JsonFile"""


import json
"""import json"""


def load_from_json_file(filename):
    """Reads from jsonfile and turns it into python objects"""
    with open(filename, 'r', encoding='utf-8') as jsfile:
        return json.load(jsfile)
