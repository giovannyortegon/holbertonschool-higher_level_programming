#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_function(fct, *args):
    res = 0
    try:
        res = fct(*args)
    except Exception as z_err:
        print("Exception: {}".format(z_err), file=sys.stderr)
    except Exception as idx_err:
        print("Exception: {}".format(idx_err), file=sys.stderr)
    else:
        return res
