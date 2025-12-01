from utils import *
inp = input_file(2016, 16).strip()

def dragon(a):
    b = a[::-1]
    b = b.replace("0", "2").replace("1", "0").replace("2", "1")
    return a + "0" + b

checksum = lambda s: "".join(["1" if s[i] == s[i + 1] else "0" for i in range(0, len(s) - 1, 2)])

def fill(size):
    disk = inp
    while len(disk) < size:
        disk = dragon(disk)
    chk = checksum(disk[:size])
    while len(chk) % 2 != 1:
        chk = checksum(chk)
    return chk

p1 = fill(272)

p2 = fill(35651584)

output(p1, p2)