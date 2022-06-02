#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv)
    b = 0
    if (i < 2):
        print("0 arguments.")
    elif (i == 2):
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    elif (i > 2):
        b = 1
        print("{} arguments:".format(i - 1))
        while (b < i):
            print("{}: {}".format(b, sys.argv[b]))
            b += 1
