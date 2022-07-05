#!/usr/bin/python3
""" Module Takes Json and Turns it into Python """


import json
""" Import Json module """


def from_json_string(my_str):
    """Returns a python object from
    from a json string"""

    return json.loads(my_str)
