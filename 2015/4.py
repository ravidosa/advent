from utils import *
import hashlib
input = open("2015/input-4.txt", "r").read()

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