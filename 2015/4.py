from utils import *
import hashlib
inp = input_file(2015, 4).strip()

res = hashlib.md5("".encode())
i = 0
while not res.hexdigest().startswith("00000"):
    i += 1
    res = hashlib.md5((inp + str(i)).encode())
p1 = i

res = hashlib.md5("".encode())
i = 0
while not res.hexdigest().startswith("000000"):
    i += 1
    res = hashlib.md5((inp + str(i)).encode())
p2 = i

output(p1, p2)