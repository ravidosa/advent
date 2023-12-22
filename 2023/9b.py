import numpy as np
f = open("2023/input-9.txt", "r")
inp = f.read().split("\n")
s = 0
for i in inp[:-1]:
    ii = np.array([int(x) for x in i.split(" ")])
    p = ii[0]
    while len(ii) > 1:
        d = np.diff(ii)
        p = d[0] - p
        ii = d
    s += p
print(s)