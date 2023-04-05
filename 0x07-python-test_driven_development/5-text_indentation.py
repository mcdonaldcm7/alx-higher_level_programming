#!/usr/bin/python3
"""
This module contains the definition for the function text_indentation.
text_indentation prints 2 new lines after the character '.', '?', and ':'
appears in the string passed to the function
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after each of these characters
    ., ?, and :
    It also contains type checks to make sure the argument passed is a string

    Parameter(s)
    ------------
    text (str): Text to print

    Example:
        >>> text_indentation("Hello.My name is McDonald:What's yours?")
        Hello.

        My name is McDonald:

        What's yours?

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    txt = ""
    for i in text:
        txt += i
        if i == '?' or i == '.' or i == ':':
            count = 0
            non_space = False
            while not non_space:
                if txt[count] == ' ':
                    count += 1
                else:
                    non_space = True
            if count > 0:
                txt = txt[count:]
            non_space = False
            count = -1
            while not non_space:
                if txt[count] == ' ':
                    count -= 1
                else:
                    non_space = True
            if count < -1:
                txt = txt[:count]
            print(txt)
            print()
            txt = ""
    count = 0
    non_space = False
    while not non_space:
        if txt[count] == ' ':
            count += 1
        else:
            non_space = True
    if count > 0:
        txt = txt[count:]
    non_space = False
    count = -1
    while not non_space:
        if txt[count] == ' ':
            count -= 1
        else:
            non_space = True
    if count < -1:
        txt = txt[:count]
    print(txt, end="")
