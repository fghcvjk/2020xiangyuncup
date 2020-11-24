from Crypto.Util.number import *
import gmpy2

p = getStrongPrime(512)
q = getStrongPrime(512)
n = p * q
phi = (p - 1) * (q - 1)
e = 7621
d = gmpy2.invert(e, phi)

flag = b"flag{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}"
c = pow(bytes_to_long(flag), e, n)

dp = d % (p - 1)
print(dp >> 200)
print(c, e, n)
