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

from pwn import *

r = remote('127.0.0.1',20000)

n = int(r.recvline().strip().split(b'= ')[1].decode())
c = int(r.recvline().strip().split(b'= ')[1].decode())
e = 65537

def oracle(c, r):
    r.sendline(str(c).encode())
    return int(r.recvline().strip().split(b'= ')[1].decode())

m = LSB_oracle_attack(n, e, c, oracle, r)

plain = long_to_bytes(m)
plain = plain[plain.rfind(b'\x00') + 1:]

print(plain)