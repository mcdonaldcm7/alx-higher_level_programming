#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return (0)
    num = 0
    prev = ''
    for i in roman_string:
        if (i == 'M'):
            if prev == 'C':
                num -= 200
            num += 1000
        elif (i == 'D'):
            if prev == 'C':
                num -= 200
            num += 500
        elif (i == 'C'):
            if prev == 'X':
                num -= 20
            num += 100
        elif (i == 'L'):
            if prev == 'X':
                num -= 20
            num += 50
        elif (i == 'X'):
            if prev == 'I':
                num -= 2
            num += 10
        elif (i == 'V'):
            if prev == 'I':
                num -= 2
            num += 5
        elif (i == 'I'):
            num += 1
        prev = i
    return (num)
