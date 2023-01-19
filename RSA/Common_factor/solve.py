from CTFlib.Crypto.RSA import *

'''
already import :

from math import gcd, ceil
from gmpy2 import iroot
from functools import reduce
from sage.all import var, Integer, NonNegativeIntegerSemiring, Zmod, PolynomialRing, IntegerRing
from Crypto.Util.number import long_to_bytes, bytes_to_long
'''

# sage : Z.<x> = PolynoamialRing(Zmod(n),implementation='NTL')
# Z = PolynomialRing(Zmod(n),implementation='NTL', names=('x',)); (x,) = Z._first_ngens(1)

# sage : Z.<x> = PolynomialRing(ZZ)
# Z = PolynomialRing(ZZ, names=('x',)); (x,) = Z._first_ngens(1)

with open('output.txt') as f:
    n1 = int(f.readline().strip().split(' = ')[1])
    n2 = int(f.readline().strip().split(' = ')[1])
    c = int(f.readline().strip().split(' = ')[1])
e = 65537

p = gcd(n1,n2)
q1 = n1 // p

m = simple_decrypt(p, q1, e, c)

plain = long_to_bytes(m)
plain = plain[plain.rfind(b'\x00') + 1:]

print(plain)