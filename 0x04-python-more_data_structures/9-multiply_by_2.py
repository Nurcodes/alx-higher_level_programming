#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for keys, val in new.items():
        new[keys] = val * 2
    return new
