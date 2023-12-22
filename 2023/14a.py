import numpy as np
f = open("2023/input-14.txt", "r")
inp = f.read().split("\n")
pat = np.array([list(x) for x in inp[:-1]], dtype="str")
load = 0
for x in range(len(pat[0])):
    l = 0
    mov = 0
    for y in range(len(pat)):
        if pat[y][x] == "#":
            mov = 0
        if pat[y][x] == "O":
            l += len(pat) - y + mov
        if pat[y][x] == ".":
            mov += 1
    load += l
print(load)