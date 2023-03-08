#!/usr/bin/python3
def uppercase(str):
    tmp = ""
    for i in str:
        asc = ord(i)
        if asc >= 97 and asc <= 122:
            tmp += chr(asc - 32)
        else:
            tmp += chr(asc)
    print("{0}".format(tmp))
