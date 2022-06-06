#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = []
    if 0 <= idx < len(my_list):
        for i in my_list:
            new.append(i)
        new[idx] = element
        return new
    new = my_list
    return new
