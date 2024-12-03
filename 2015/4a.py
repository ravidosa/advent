import hashlib

f = open("2015/input-4.txt", "r")
inp = f.read()

res = hashlib.md5("".encode())
i = 0
while (not res.hexdigest().startswith("00000")):
    i += 1
    res = hashlib.md5((inp + str(i)).encode())
print(i)