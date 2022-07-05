#!/usr/bin/python3
""" This module uses f.write to a file """


def write_file(filename="", text=""):
    """ returns number of of characters printed to the file """

    with open(filename, 'w', encoding='utf-8') as f:
        """ return f.write """
        return f.write(text)
