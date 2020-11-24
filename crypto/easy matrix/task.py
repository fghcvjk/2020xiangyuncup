import numpy as np
from secret import *

def random_offset(size):
    x = np.random.normal(0, 4.7873, size)
    return np.rint(x)



secret = np.array(list(flag))

column = len(list(secret))
row = 128
prime = 2129

matrix = np.random.randint(512, size=(row, column))
product = matrix.dot(secret) % prime
offset = random_offset(size=row).astype(np.int64)
result = (product + offset) % prime

np.save("matrix.npy", matrix)
np.save("result.npy", result)


