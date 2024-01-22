#!/usr/bin/python3

import sys
from __future__ import print_function

def safe_function(fct, *args):


    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
