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


def get_value(code):
    
    
def shell_loop(*args, **kwargs):
    try:
        code = input(":: ").strip()

        if not code: return 0

        cmd, *args = code.split(" ")
        
        if is_assembly(cmd): 
            op = OP_TABLE[cmd]
            args = list(map(int, args))
            
        else:
            cmd = BIN(cmd, BITS, str)
            op = OP_TABLE[cmd.int]
            args = list(map((lambda x : BIN(x, BITS, str)), args))

        print("cmd:", cmd, "\nargs:", args)

    except KeyboardInterrupt:
        return 1
        
    except Error as e:
        print(e)
    
    return 0

def shell(*args, **kwargs):
    while not shell_loop(*args, **kwargs):
        continue
    else:
        return 0

def main(argc, argv):
    global BITS
    
    print(__doc__)
    
    if not shell(argc, argv):
        return 0

if __name__ == '__main__':
    main(argc, argv)
