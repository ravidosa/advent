import numpy as np
f = open("2023/input-9.txt", "r")
inp = f.read().split("\n")
s = 0
for i in inp[:-1]:
    ii = np.array([int(x) for x in i.split(" ")])
    p = ii[-1]
    while np.any(ii):
        d = np.diff(ii)
        p += d[-1]
        ii = d
    s += p
print(s)