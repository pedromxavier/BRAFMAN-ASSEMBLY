#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
  +-+-+-+-+-+-+-+
  |B|R|A|F|M|A|N|
 +-+-+-+-+-+-+-+-+
 |A|S|S|E|M|B|L|Y|
 +-+-+-+-+-+-+-+-+
      v 1.1
"""
import sys, os

argv = sys.argv
argc = len(argv)

from braf import *

def get_cmd(cmd):
    if cmd.endswith("H"):
        cmd_key = int(cmd[:-1], 16)
    if

    if cmd_key not in OP_TABLE:
        raise NameError("Invalid OP {}".format(cmd))
    else:
        return OP_TABLE[cmd_key]

def get_arg(arg):
    ...

def exec_cmd(op, args):
    return op(*args)

def shell_loop(*args, **kwargs):
    try:
        code = input(":: ").strip().upper()

        if not code: return 0

        cmd, *args = code.split(" ")

        cmd = get_cmd(cmd)

        args = map(get_arg, args)

        print(exec_cmd(cmd, args))

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
