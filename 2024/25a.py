f = open("2024/input-25.txt", "r")
inp = [ff.split("\n") for ff in f.read().split("\n\n")]

locks = []
keys = []

w, h = len(inp[0][0]), len(inp[0]) - 2

for i in inp:
    if all([ii == "#" for ii in i[0]]):
        hei = [0] * w
        for j in range(1, h + 1):
            hei = [hei[k] + (i[j][k] == "#") for k in range(w)]
        locks.append(hei)
    if all([ii == "." for ii in i[0]]):
        hei = [0] * w
        for j in range(h, 0, -1):
            hei = [hei[k] + (i[j][k] == "#") for k in range(w)]
        keys.append(hei)

val = 0
for lock in locks:
    for key in keys:
        if all([(lock[k] + key[k]) <= h for k in range(w)]):
            val += 1
print(val)