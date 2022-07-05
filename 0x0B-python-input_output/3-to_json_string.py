#!/usr/bin/python3
""" Takes python object and returns json string """


import json
""" Importing Json module """


def to_json_string(my_obj):
    """ Returns Json of python object """

    return json.dumps(my_obj)
