from Crypto.Util.number import *
from gmpy2 import next_prime

p = getPrime(512)
q = getPrime(512)

n = p * q * next_prime(p) * next_prime(q)
e = 0x10001

flag = b"flag{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}"
cipher = pow(bytes_to_long(flag), e, n)

print(n, cipher)