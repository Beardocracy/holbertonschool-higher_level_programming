#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    if args is None or len(args) == 0:
        return None

    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
