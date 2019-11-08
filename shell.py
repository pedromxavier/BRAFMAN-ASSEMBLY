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

import braf.table as table

memory = {}

regs = {}

class BIN(list):

    def __init__(self, buffer, bits=4, dtype=int):
        self.bits = bits

        if dtype is int:
            pass
        elif dtype is oct:
            buffer = int(buffer, 8)
        elif dtype is hex:
            buffer = int(buffer, 16)
        elif dtype is str:
            buffer = int(str)
        elif dtype is BIN:
            pass
        else:
            raise TypeError("Invalid Data Type {}.".format(dtype)

        buffer = BIN.int_to_bin(buffer, bits)

        self.overflow = (self.int > pow(2, self.bits))

    def __getitem__(self, i):
        return list.__getitem__(reversed(self), i)

    @staticmethod
    def int_to_bin(buffer, bits)
        return map(int, bin(buffer)[2:].zfill(bits))

    @staticmethod
    def flags(buffer, bits):
        
        # zero
        z = (buffer.int == 0)
        
        #negative
        n = (buffer.int < 0)

        #carry
        c = (buffer.bits > bits and buffer[bits + 1] == 1)

    def __add__(a, b):
        assert a.bits = b.bits

        c = BIN(a.int + b.int, a.bits, dtype=int)

        return c, BIN.flags(c, a.bits)

    def __mul__(a, b):
        assert a.bits == b.bits

        c =  BIN(a.int * b.int, a.bits + b.bits, dtype=int)

        return c, BIN.flags(c, a.bits + b.bits)

def shell(*args, **kwargs):
    
    while True:
        code = input(":: ")

        cmd, *args = map(BIN, code.split(" "))




def main(argc, argv):
    ...

if __name__ == '__main__':
    main(argc, argv)
