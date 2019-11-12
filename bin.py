import random
import error

class BIN(list):

    BITS = 4

    def __init__(self, buffer=None, bits=None, dtype=int, **flags):

        self.__flags = {k : (flags[k] if k in flags else None) for k in 'zncv'}

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

        sig = (buffer < 0)

        if sig: ## Negative
            mod = abs(buffer + 1)
        else:
            mod = abs(buffer)

        mod_buffer = map(int, bin(mod)[-1:1:-1])

        if sig:
            new_buffer = [not x for x in mod_buffer] + [sig]
        else:
            new_buffer = list(mod_buffer) + [sig]

        return new_buffer

    def __add__(a, b):
        assert a.bits == b.bits

        c = [False] * (a.bits + 1) ## Carry
        buffer = [False] * (a.bits)

        for i in range(a.bits):
            buffer[i] = ((a[i] ^ b[i]) ^ c[i])
            c[i+1] = ((a[i] & b[i]) | (a[i] & c[i]) | (b[i] & c[i]))

        flags = {
            'c' : c[-1],
            'v' : c[-1] ^ c[-2],
        }

        return BIN(buffer, a.bits, dtype=BIN, **flags)

    def __sub__(a, b):
        return a + b.cmp

    def __and__(a, b):
        assert a.bits == b.bits
        buffer = [x & y for x,y in zip(a,b)]

        flags = {
            'c' : False,
            'v' : False,
        }

        return BIN(buffer, a.bits, dtype=BIN, **flags)

    def __lshift__(a, _):
        buffer = [False] + [a[i] for i in range(0, a.bits-1)]

        flags = {
            'c' : a[-1],
            'v' : False,
        }

        return BIN(buffer, a.bits, dtype=BIN, **flags)

    def __rshift__(a, _):
        buffer = [a[i] for i in range(1, a.bits)] + [a[-1]]

        flags = {
            'c' : False,
            'v' : False,
        }

        return BIN(buffer, a.bits, dtype=BIN, **flags)

    def __or__(a, b):
        assert a.bits == b.bits
        buffer = [x | y for x,y in zip(a,b)]

        flags = {
            'c' : False,
            'v' : False,
        }

        return BIN(buffer, a.bits, dtype=BIN, **flags)

    def __xor__(a, b):
        assert a.bits == b.bits
        buffer = [x ^ y for x,y in zip(a,b)]

        flags = {
            'c' : False,
            'v' : False,
        }

        return BIN(buffer, a.bits, dtype=BIN, **flags)

    def __invert__(a):
        buffer = [not x for x in a]

        flags = {
            'c' : False,
            'v' : False,
        }

        return BIN(buffer, a.bits, dtype=BIN, **flags)

    @property
    def flags(self):
        return (self.z, self.n, self.c, self.v)

    @property
    def z(self):
        return (self.int == 0)

    @property
    def n(self):
        return (self.int < 0)

    @property
    def c(self):
        return self.__flags['c']

    @property
    def v(self):
        return self.__flags['v']

    @property
    def int(self):
        if self[-1]: ## Negative
            return -self.cmp.int
        else:
            return sum([self[j] * pow(2, j) for j in range(self.bits-1)])

    @property
    def cmp(self):

        flags = {
            'c' : False,
            'v' : False,
        }

        return ~self + BIN(1, self.bits, dtype=int, **flags)
