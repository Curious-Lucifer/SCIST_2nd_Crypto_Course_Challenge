from CTFlib.Crypto.RSA import *

'''
already import :

from math import gcd
from gmpy2 import iroot
from functools import reduce
from sage.all import var, Integer, NonNegativeIntegerSemiring, Zmod, PolynomialRing, IntegerRing, ceil, floor
from Crypto.Util.number import long_to_bytes, bytes_to_long
'''

# sage : Z.<x> = PolynoamialRing(Zmod(n),implementation='NTL')
# Z = PolynomialRing(Zmod(n),implementation='NTL', names=('x',)); (x,) = Z._first_ngens(1)

# sage : Z.<x> = PolynomialRing(ZZ)
# Z = PolynomialRing(ZZ, names=('x',)); (x,) = Z._first_ngens(1)

with open('output.txt') as f:
    n = int(f.readline().strip().split(' = ')[1])
    c = int(f.readline().strip().split(' = ')[1])
e = 3

for i in range(1,126):
    mbar = bytes_to_long(b'\x00' + b'\xff' * i + b'\x00' * (127 - i))
    x0 = stereotyped_message(mbar, c, e, n, epsilon= 1 / Integer(16))
    if (x0 != -1) and (long_to_bytes(x0).startswith(b'CTF{')):
        print(long_to_bytes(x0))
        break