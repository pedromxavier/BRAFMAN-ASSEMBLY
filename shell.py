#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 __  __      __
|__)|__) /\ |_ |\/| /\ |\ |
|__)| \ /--\|  |  |/--\| \|

     __ __ __     __
 /\ (_ (_ |_ |\/||__)| \_/
/--\__)__)|__|  ||__)|__|


          v1.0.0

        08/11/2019
"""
import sys, os

argv = sys.argv
argc = len(argv)

from braf import *


def is_assembly(cmd):
    return any(x not in {0,1} for x in cmd)

def shell(*args, **kwargs):

    try:
        while True:
            code = input(":: ").strip()

            if not code: continue

            cmd, *args = map((lambda x : BIN(x, BITS, str)), code.split(" "))

            if cmd.int in OP_TABLE:
                OP_TABLE[cmd.int](*args)

            print("cmd:", cmd, "\nargs:", args)

    except KeyboardInterrupt:
        return 0

def main(argc, argv):
    global BITS
    
    print(__doc__)
    
    if not shell(argc, argv):
        return 0

if __name__ == '__main__':
    main(argc, argv)
