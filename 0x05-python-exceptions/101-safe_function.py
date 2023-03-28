#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    ret = None
    try:
        ret = fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return (None)
    return (ret)
