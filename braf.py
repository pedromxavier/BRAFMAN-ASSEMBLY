#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
"""

OP_TABLE = {}

MEMORY = {}

REG = {}

def cmd(f, at=None):
        """
        """
        global OP_TABLE

        if at is not None :
            OP_TABLE[at] = f
            
        OP_TABLE[f.__name__] = f    

        return f

def cmd_at(at):
    return lambda f : cmd(f, at)

@cmd_at(0b0000)
def NO_OP():
    pass

@cmd_at(0b0001)
def ADD(A, B, C):
    global REG
    REG[A] = REG[B] + REG[C]

@cmd_at(0b0010)
def SUB(A, B, C):
    global REG
    REG[A] = REG[B] - REG[C]    

@cmd_at(0b0011)
def MUL(A, B, C):
    global REG
    REG[A] = REG[B] * REG[C]

BITS = 4

class BIN(list):

    def __init__(self, buffer, bits=BITS, dtype=int):
        self.bits = bits

        int_buffer = None

        if dtype is int:
            int_buffer = buffer
        elif dtype is oct:
            int_buffer = int(buffer, 8)
        elif dtype is hex:
            int_buffer = int(buffer, 16)
        elif dtype is str:
            int_buffer = int(buffer, 2)
        elif dtype is BIN:
            pass
        else:
            raise TypeError("Invalid Data Type {}.".format(dtype))

        if int_buffer is not None:
            buffer = BIN.int_to_bin(int_buffer, bits)

        list.__init__(self, buffer)

        self.overflow = (self.int > pow(2, self.bits))

    def __getitem__(self, i):
        return list.__getitem__(list(reversed(self)), i)

    def __hash__(self):
        return self.int

    def __str__(self):
        return "".join(map(str, self))

    def __repr__(self):
        return "".join(map(str, self))        

    @staticmethod
    def int_to_bin(buffer, bits):
        return map(int, bin(buffer)[2:].zfill(bits))

    @staticmethod
    def flags(buffer, bits):
        
        # zero
        z = (buffer.int == 0)
        
        #negative
        n = (buffer.int < 0)

        #carry
        c = (buffer.bits > bits and buffer[bits + 1] == 1)

        #overflow
        v = (c and buffer[-1] == 1)

        return z, n, c, v                    

    def __add__(a, b):
        assert a.bits == b.bits

        c = BIN(a.int + b.int, a.bits, dtype=int)

        return c, BIN.flags(c, a.bits)

    def __mul__(a, b):
        assert a.bits == b.bits

        c =  BIN(a.int * b.int, a.bits + b.bits, dtype=int)

        return c, BIN.flags(c, a.bits + b.bits)

    def __sub__(a, b):
        assert a.bits == b.bits

        c = BIN(a.int - b.int, a.bits, dtype=int)

        return c, BIN.flags(c, a.bits)

    @property
    def int(self):
        return sum([self[j] * pow(2, j) for j in range(self.bits)])
