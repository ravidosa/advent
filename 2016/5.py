from utils import *
import hashlib
input = input_file(2016, 5).strip()

password = ""
i = 0
while len(password) < 8:
    res = hashlib.md5("".encode())
    while not res.hexdigest().startswith("00000"):
        i += 1
        res = hashlib.md5((input + str(i)).encode())
    password += res.hexdigest()[5]
print(password)

password = [None] * 8
i = 0
while None in password:
    res = hashlib.md5("".encode())
    while not res.hexdigest().startswith("00000"):
        i += 1
        res = hashlib.md5((input + str(i)).encode())
    if res.hexdigest()[5] in "01234567" and password[int(res.hexdigest()[5])] == None:
        password[int(res.hexdigest()[5])] = res.hexdigest()[6]
print("".join(password))