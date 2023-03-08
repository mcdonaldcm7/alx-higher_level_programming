#!/usr/bin/python3
def remove_char_at(str, n):
    rem = ""
    for i in range(0, len(str)):
        if i == n:
            continue
        rem += str[i]
    return (rem)
