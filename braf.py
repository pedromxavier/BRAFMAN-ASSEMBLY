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

class Reg(list):

    def __init__(self, regs, bits):
        list.__init__(self, [BIN(bits=bits) for _ in range(regs)])


    def __getitem__(self, key):
        try:
            list.__getitem__(self, key)
        except IndexError:
            msg = "No register in position {} [{}]".format(key,bin(key))
            raise Error(msg)

OP_TABLE = {}

MEMORY = Memory(SIZE, BITS)

REG = Reg(REGS, BITS)

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
    global REG
    REG[A] = REG[B] + REG[C]

@cmd_at(0b010001)
def ADI(A, B, C):
    global REG
    REG[A] = REG[B] + C

@cmd_at(0b010010)
def SUB(A, B, C):
    global REG
    REG[A] = REG[B] - REG[C]

@cmd_at(0b010011)
def SBI(A, B, C):
    global REG
    REG[A] = REG[B] - C

@cmd_at(0b010100)
def AND(A, B, C):
    global REG
    REG[A] = REG[B] & REG[C]

@cmd_at(0b010101)
def ANI(A, B, C):
    global REG
    REG[A] = REG[B] & C

@cmd_at(0b010110)
def OR(A, B, C):
    global REG
    REG[A] = REG[B] | REG[C]

@cmd_at(0b010111)
def ORI(A, B, C):
    global REG
    REG[A] = REG[B] | C

@cmd_at(0b011000)
def XOR(A, B, C):
    global REG
    REG[A] = REG[B] ^ REG[C]

@cmd_at(0b011001)
def XRI(A, B, C):
    global REG
    REG[A] = REG[B] ^ C
