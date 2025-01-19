from utils import *
import hashlib
input = input_file(2015, 4).strip()

res = hashlib.md5("".encode())
i = 0
while not res.hexdigest().startswith("00000"):
    i += 1
    res = hashlib.md5((input + str(i)).encode())
print(i)

res = hashlib.md5("".encode())
i = 0
while not res.hexdigest().startswith("000000"):
    i += 1
    res = hashlib.md5((input + str(i)).encode())
print(i)