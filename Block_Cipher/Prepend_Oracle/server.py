# socat TCP-LISTEN:20000,fork EXEC:"python3 server.py"
import os
from Crypto.Cipher import AES

KEY = os.urandom(16)
FLAG = open('./flag', 'rb').readline().strip()

def pad(m):
    padlen = -len(m) % 16
    return m + bytes([0] * padlen)

def main():
    aes = AES.new(KEY, AES.MODE_ECB)
    
    while True:
        message = bytes.fromhex(input('message = ').strip())
        cipher = aes.encrypt(pad(message + FLAG))
        print(f'cipher = {cipher.hex()}')

try:
    main()
except:
    pass
