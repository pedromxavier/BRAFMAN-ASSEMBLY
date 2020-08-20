class bitarray(object):

    twos_comp = False

    def __init__(self, bits: int, **flags):
        self.bits = bits
        self._array = [False] * bits

        self._flags = {**flags}

    def __getitem__(self, i: int):
        assert type(i) is int and 1 <= i <= self.bits
        return int(self._array[i-1])

    def __setitem__(self, i: int, x: bool):
        assert type(i) is int and 1 <= i <= self.bits
        self._array[i-1] = bool(x)

    def __iter__(self):
        return iter(self._array)

    def __repr__(self):
        return str(self) # return f"{type(self).__name__}({self.bits}, {int(self)})"

    def __str__(self):
        return str([int(x) for x in reversed(self._array)])
    
    def __int__(self):
        if self.twos_comp:
            return (1 if not self[self.bits] else -1) * sum(x * pow(2, i) for i, x in enumerate(self._array[:self.bits-1]))
        else:
            return sum(x * pow(2, i) for i, x in enumerate(self._array))

    # Logical
    def __and__(self, other):
        res = type(self)(self.bits)
        for i in range(self.bits):
            res._array[i] = self._array[i] & other._array[i]
        return res

    def __or__(self, other):
        res = type(self)(self.bits)
        for i in range(self.bits):
            res._array[i] = self._array[i] | other._array[i]
        return res

    def __xor__(self, other):
        res = type(self)(self.bits)
        for i in range(self.bits):
            res._array[i] = self._array[i] ^ other._array[i]
        return res

    def __invert__(self):
        res = type(self)(self.bits)
        for i in range(self.bits):
            res._array[i] = not self._array[i]
        return res

    # Arithmetic
    def __add__(self, other):
        res = type(self)(self.bits)
        carry = [False] * (self.bits + 1)
        for i in range(self.bits):
            res._array[i] = (self._array[i] ^ other._array[i]) ^ carry[i]
            carry[i + 1] = (self._array[i] & other._array[i]) | ((self._array[i] & carry) ^ (other._array[i] & carry))
        res._flags['C'] = carry[i + 1] ## carry
        res._flags['O'] = carry[i + 1] ^ carry[i] ## overflow
        return res

    @classmethod
    def set_twos_comp(cls, active: bool):
        cls.twos_comp = bool(active)

    @property
    def index(self):
        return range(1, self.bits + 1)


class Register(object):

    __ref__ = {}

    bits = 8

    def __new__(cls, num: int):
        assert type(num) is int

        if num not in cls.__ref__:
            register = object.__new__(cls)
            cls.__init__(register, num)
            cls.__ref__[num] = register
        return cls.__ref__[num]

    def __init__(self, num: int):
        self.num = num
        self.val = bitarray(self.bits)

    def __str__(self):
        return f"R{self.num}"

    def __repr__(self):
        return f"Register({self.num})"