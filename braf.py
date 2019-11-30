#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
"""
import sys
import random

from bin import BIN

from error import Error

argv = sys.argv
argc = len(argv)

SIZE = 32
BYTES = 4
REGS = 32

class _Memory(list):

    SIZE = SIZE;
    BITS = 8 * BYTES;

    __ref__ = None

    def __new__(cls):
        if cls.__ref__ is None:
            self = list.__new__(cls)
            cls.__init__(self)
            cls.__ref__ = self
        return cls.__ref__

    def __init__(self):
        list.__init__(self, [BIN(bits=self.BITS) for _ in range(self.SIZE)])

    def __setitem__(self, key_bytes, val):
        key, bytes = key_bytes

class _Register[list):

    REGS = REGS;
    BITS = 8 * BYTES;

    __ref__ = None

    def __new__(cls):
        if cls.__ref__ is None:
            self = list.__new__(cls)
            cls.__init__(self)
            cls.__ref__ = self
        return cls.__ref__

    def __init__(self):
        list.__init__(self, [BIN(bits=self.BITS) for _ in range(self.REGS)])
        self.PC = BIN(bits=self.BITS)

    def __getitem__(self, key):
        if key == None:
            return self.PC
        elif (not 0 <= key < cls.REGS):
            msg = "No register {}".format(key)
            raise Error(msg)
        else:
            return list.__getitem__(self, key)

    def __setitem__(self, key, val):
        if key == None:
            self.PC = val
        elif (not 0 <= key < cls.REGS):
            msg = "No register {}".format(key)
            raise Error(msg)
        else:
            return list.__setitem__(self, key, val)

    def __init__(self, key):
        self.key = key
        self.bin = BIN(bits=self.BITS)

    def __repr__(self):
        return "R{}".format(self.key)

    def __lt__(A, X):
        if type(X) is Register:
            A.bin = X.bin
        elif type(X) is int:
            A.bin = X

    def __add__(A, B):
        if type(B) is Register:
            return A.bin + B.bin
        elif type(B) is int:
            return A.bin + B

    def __sub__(A, B):
        if type(B) is Register:
            return A.bin - B.bin
        elif type(B) is int:
            return A.bin - B

Register = _Register()
Register.PC < 0x000000;

Memory = _Memory()

OP_TABLE = {}

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

## OPS

@cmd_at(0b000000)
def NOP():
    pass

@cmd_at(0b000010)
def NOT(RA, RB):
    Register[RA] = ~Register[RB]

@cmd_at(0b000100)
def LSH(RA, RB):
    Resgiter[RA] = Register[RB] << 0

@cmd_at(0b000110)
def RSH(RA, RB):
    Resgiter[RA] = Register[RB] >> 0

@cmd_at(0b001000)
def LRT(RA, RB):
    Resgiter[RA] = Register[RB] << 1

@cmd_at(0b001010)
def RRT(RA, RB):
    Resgiter[RA] = Register[RB] >> 1

@cmd_at(0b010000)
def ADD(RA, RB, RC):
    Register[A] = Register[B] + Register[C]

@cmd_at(0b010001)
def ADI(RA, RB, RC):
    Register[A] = Register[B] + C

@cmd_at(0b010010)
def SUB(RA, RB, RC):
    Register[A] = Register[B] - Register[C]

@cmd_at(0b010011)
def SBI(RA, RB, RC):
    Register[A] = Register[B] - C

@cmd_at(0b010100)
def AND(RA, RB, RC):
    Register[A] = Register[B] & Register[C]

@cmd_at(0b010101)
def ANI(RA, RB, RC):
    Register[A] = Register[B] & C

@cmd_at(0b010110)
def OR(RA, RB, RC):
    Register[A] = Register[B] | Register[C]

@cmd_at(0b010111)
def ORI(RA, RB, C):
    Register[RA] = Register[RB] | C

@cmd_at(0b011000)
def XOR(RA, RB, RC):
    Register[RA] = Register[RB] ^ Register[RC]

@cmd_at(0b011001)
def XRI(RA, RB, C):
    Register[RA] = Register[RB] ^ C

@cmd_at(0b100011)
def STW(RA, D_RB):
    D, RB = D_RB

class Compiler:

    def __init__(self, table, *args, **kwargs):
        self.table = table

    def __call__(self, code):
        res = []
        for cmd, args in code:
            if cmd not in self.table:
                print('SyntaxError: Unkown {}'.format(cmd))
                raise SyntaxError()
            else:
                res.append((self.table[cmd], args))
        return res

compiler = Compiler(OP_TABLE)

def run(code, compiler):
    for cmd, args in compiler(code):
        cmd(*args)
