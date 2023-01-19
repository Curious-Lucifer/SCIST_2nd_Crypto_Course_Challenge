from CTFlib.Crypto.RSA import *
from CTFlib.Crypto.Block_Cipher import *

'''
already import :

from math import gcd
from gmpy2 import iroot
from functools import reduce
from sage.all import var, Integer, NonNegativeIntegerSemiring, Zmod, PolynomialRing, IntegerRing, ceil, floor, GF
from Crypto.Util.number import long_to_bytes, bytes_to_long
from pwn import xor
'''

# sage : Z.<x> = PolynoamialRing(Zmod(n),implementation='NTL')
# Z = PolynomialRing(Zmod(n),implementation='NTL', names=('x',)); (x,) = Z._first_ngens(1)

# sage : Z.<x> = PolynomialRing(ZZ)
# Z = PolynomialRing(ZZ, names=('x',)); (x,) = Z._first_ngens(1)

from pwn import *

r =  remote('127.0.0.1', 20000)

def oracle(cipher, r):
    r.sendlineafter(b'= ', cipher.hex().encode())
    return bytes.fromhex(r.recvline().strip().split(b'= ')[1].decode())

flag_length = len(oracle(b'', r))
for i in range(1,17):
    if len(oracle(b'a' * i, r)) != flag_length:
        flag_length -= i - 1
        break

flag = prepend_oracle_attack(flag_length, oracle, r)

print(flag)

r.interactive()