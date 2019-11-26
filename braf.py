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
BITS = 32
REGS = 32

class Memory(list):

    def __init__(self, size, bits):
        list.__init__(self, [BIN(bits=bits) for _ in range(size)])

    def __getitem__(self, key):
        try:
            list.__getitem__(self, key)
        except IndexError:
            msg = "No memory address {} [{}]".format(key,bin(key))
            raise Error(msg)

class Register(object):

    REGS = REGS;
    BITS = BITS;

    PC = -1;

    __ref__ = {}

    def __new__(cls, key):
        if (not 0 <= key < cls.REGS) and (key != -1):
            msg = "No register {}".format(key)
            raise Error(msg)
        else:
            if key not in cls.__ref__:
                self = object.__new__(cls)
                cls.__init__(self, key)
                cls.__ref__[key] = self
            return cls.__ref__[key]

    def __init__(self, key):
        self.key = key
        self.val = random.randint(0, pow(2,self.BITS)-1)

    def __repr__(self):
        return "R{}".format(self.key)

    def __lt__(A, X):
        if type(X) is Register:
            A.val = X.val
        elif type(X) is int:
            A.val = X

    def __add__(A, B):
        if type(B) is Register:
            return A.val + B.val
        elif type(B) is int:
            return A.val + B

    def __sub__(A, B):
        if type(B) is Register:
            return A.val - B.val
        elif type(B) is int:
            return A.val - B

Register(Register.PC) < 0

OP_TABLE = {}

MEMORY = Memory(SIZE, BITS)

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
def NOT():
    pass

@cmd_at(0b000100)
def LSH():
    pass

@cmd_at(0b000110)
def RSH():
    pass

@cmd_at(0b001000)
def LRT():
    pass

@cmd_at(0b001010)
def RRT():
    pass

@cmd_at(0b010000)
def ADD(A, B, C):
    Register(A) < (Register(B) + Register(C))

@cmd_at(0b010001)
def ADI(A, B, C):
    Register(A) < (Register(B) + C)

@cmd_at(0b010010)
def SUB(A, B, C):
    Register(A) < (Register(B) - Register(C))

@cmd_at(0b010011)
def SBI(A, B, C):
    Register(A) < (Register(B) - C)

@cmd_at(0b010100)
def AND(A, B, C):
    Register(A) < (Register(B) & Register(C))

@cmd_at(0b010101)
def ANI(A, B, C):
    Register(A) < (Register(B) & C)

@cmd_at(0b010110)
def OR(A, B, C):
    Register(A) < (Register(B) | REG(C))

@cmd_at(0b010111)
def ORI(RA, RB, C):
    Register(RA) < (Register(RB) | C)

@cmd_at(0b011000)
def XOR(RA, RB, RC):
    Register(RA) < (Register(RB) ^ Register(RC))

@cmd_at(0b011001)
def XRI(RA, RB, C):
    Register(RA) < (Register(RB) ^ C)

@cmd_at(0b100011)
def STW(RA, D_RB):
    D, RB = D_RB
    pass

class Compiler:

    def __init__(self, table, *args, **kwargs):
        self.table = table

    def __call__(self, code):
        res = []
        for cmd, args in code:
            if cmd not in self.table:
                print('Unkown {}'.format(cmd))
                raise SyntaxError()
            else:
                res.append((self.table[cmd], args))
        return res

compiler = Compiler(OP_TABLE)

def run(code, compiler):
    for cmd, args in compiler(code):
        cmd(*args)
