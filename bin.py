import random
import error

class BIN(list):
    
    BITS = 4

    def __init__(self, buffer=None, bits=None, dtype=int):
        if bits is None:
            self.bits = BIN.BITS
        else:
            self.bits = bits

        int_buffer = None
        
        if buffer is None:
            buffer = [random.randint(0,1) for _ in range(self.bits)]
            dtype = BIN

        if dtype is int:
            int_buffer = buffer
        elif dtype is oct:
            int_buffer = int(buffer, 8)
        elif dtype is hex:
            int_buffer = int(buffer, 16)
        elif dtype is bin:
            int_buffer = int(buffer, 2)
        elif dtype is str:
            int_buffer = int(buffer)
        elif dtype is BIN:
            pass
        elif dtype is list:
            buffer = buffer[::-1]
        else:
            raise TypeError("Invalid Data Type {}.".format(dtype))

        if int_buffer is not None:
            buffer = BIN.int_to_bin(int_buffer)
            
        list.__init__(self, BIN.bfill(buffer, self.bits))
        
        ## Flags
        
        # ZERO
        self.z = (self.int == 0)
        
        # NEGATIVE
        self.n = (self.int < 0)
        
        # CARRY
        self.c = (len(buffer) > self.bits and buffer[self.bits] == 1)
        
        # OVERFLOW
        self.v = (self.c ^ buffer[-2]) 

    @staticmethod
    def bfill(buffer, bits):
        size = min(len(buffer), bits)
        
        new_buffer = [buffer[-1]] * bits
        new_buffer[:size] = buffer[:size]
        
        return map(bool, new_buffer)


    def __hash__(self):
        return self.int

    def __str__(self):
        return "".join(map(str, map(int, self[::-1])))

    def __repr__(self):
        return str(self)      

    @staticmethod
    def int_to_bin(buffer):
        
        sig = int(buffer < 0)
        
        mod = abs(buffer)
        
        return list(map(int, bin(mod)[-1:1:-1])) + [sig]
        

    @property
    def flags(self):
        return self.z, self.n, self.c, self.v                    

    def __add__(a, b):
        assert a.bits == b.bits

        c =  BIN(a.int + b.int, a.bits, dtype=int)

        return c

    def __sub__(a, b):
        assert a.bits == b.bits

        c = BIN(a.int - b.int, a.bits, dtype=int)

        return c
        
    def __and__(a, b):
        assert a.bits == b.bits
        buffer = [x & y for x,y in zip(a,b)]
        return BIN(buffer, a.bits, dtype=BIN)
        
    def __or__(a, b):
        assert a.bits == b.bits
        buffer = [x | y for x,y in zip(a,b)]
        return BIN(buffer, a.bits, dtype=BIN)
        
    def __xor__(a, b):
        assert a.bits == b.bits
        buffer = [x ^ y for x,y in zip(a,b)]
        return BIN(buffer, a.bits, dtype=BIN)
        
    def __invert__(a):
        buffer = [not x for x in a]
        return BIN(buffer, a.bits, dtype=BIN)

    @property
    def int(self):
        mod = sum([self[j] * pow(2, j) for j in range(self.bits-1)])
        sig = pow(-1, self[-1])
        return sig * mod
        
    @property
    def cmp(self):
        return ~self + BIN(1, self.bits, dtype=int)
