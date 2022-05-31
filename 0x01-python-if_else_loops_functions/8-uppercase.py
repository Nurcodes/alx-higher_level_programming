#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if str[i] == ' ':
            print(" ", end='')
        elif str[i] > 64 and str[i] < 91:
            continue
        else:
            print("{:c}".format(ord(str[i]) - 32), end='')
