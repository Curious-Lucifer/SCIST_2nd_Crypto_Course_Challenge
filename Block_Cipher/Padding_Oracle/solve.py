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

r = remote('127.0.0.1', 20000)

iv_flag_enc = bytes.fromhex(r.recvline().strip().split(b' = ')[1].decode())
iv = iv_flag_enc[:16]

def oracle(cipher, r):
    r.sendlineafter(b'= ', (iv + cipher).hex().encode())
    return b'CORRECT' in r.recvline()

plain = b''
for i in range(0, len(iv_flag_enc) - 16, 16):
    plain += padding_oracle_attack(iv_flag_enc[i:i + 16], iv_flag_enc[i + 16:i + 32], oracle, r)

print(plain)

r.interactive()