#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        out = fct(*args)
        return out
    except (ValueError, ZeroDivisionError, TypeError, IndexError):
        print("Exception: {}".format(sys_exc_info()[1]), file=sys.stderr)
        return None

