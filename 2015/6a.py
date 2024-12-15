import re

f = open("2015/input-6.txt", "r")
inp = f.read().split("\n")

l = [[0 for _ in range(1000)] for _ in range(1000)]

for i in inp:
    s, f = i.split(" through ")
    ix, iy = [int(x) for x in re.sub('toggle |turn off |turn on ', '', s).split(",")]
    fx, fy = [int(x) for x in f.split(",")]
    for x in range(ix, fx + 1):
        for y in range(iy, fy + 1):
            if i.startswith("turn on"):
                l[y][x] = 1
            if i.startswith("turn off"):
                l[y][x] = 0
            if i.startswith("toggle"):
                l[y][x] = 1 - l[y][x]

print(sum([sum(ll) for ll in l]))