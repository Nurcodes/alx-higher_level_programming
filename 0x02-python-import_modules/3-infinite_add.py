#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l_en = len(sys.argv)
    b = 0
    s_um = 0
    if (l_en == 1):
        print("0")
    elif (l_en > 1):
        b = 1
        while (b < l_en):
            s_um += int(sys.argv[b])
            b += 1
        print(s_um)
