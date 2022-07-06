#!/usr/bin/python3
"""Writes an object to a text file, using json representation"""


import json
"""import json"""


def save_to_json_file(my_obj, filename):
    """ saves a file through with and json """

    with open(filename, 'w', encoding='utf-8') as f:
        """ use open and with to write """
        f.write(json.dumps(my_obj))
