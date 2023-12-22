import numpy as np
f = open("2023/input-11.txt", "r")
inp = f.read().split("\n")
gal = np.array([list(i) for i in inp[:-1]], dtype="str")
m, n = len(gal[0]), len(gal)
empr = np.array(list(filter(lambda x: "#" not in gal[:,x], list(range(m)))))
empc = np.array(list(filter(lambda x: "#" not in gal[x,:], list(range(n)))))
exp = 2
gals = []
for y in range(n):
    for x in range(m):
        if gal[y][x] == "#":
            gals.append((x, y))
s = 0
for i, g in enumerate(gals):
    for gg in gals[i + 1:]:
        s += abs(g[0] - gg[0]) + abs(g[1] - gg[1]) + (exp - 1) * (len(empr[(min(g[0], gg[0]) < empr) & (empr < max(g[0], gg[0]))]) + len(empc[(min(g[1], gg[1]) < empc) & (empc < max(g[1], gg[1]))]))
print(s)