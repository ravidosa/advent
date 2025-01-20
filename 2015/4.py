from utils import *
import hashlib
inp = input_file(2015, 4).strip()

def hash_zeros(n):
    res = hashlib.md5("".encode())
    i = 0
    while not res.hexdigest().startswith("0" * n):
        i += 1
        res = hashlib.md5((inp + str(i)).encode())
    return i

p1 = hash_zeros(5)

p2 = hash_zeros(6)

output(p1, p2)