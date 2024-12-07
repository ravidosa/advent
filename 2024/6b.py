import re

f = open("2024/input-6.txt", "r")
inp = f.read().split("\n")

vis = set()
x, y = "".join(inp).index("^") % len(inp[0]), "".join(inp).index("^") // len(inp[0])
ix, iy = x, y

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dir = 0
vis.add((x, y))

while x != 0 and x != len(inp[0]) - 1 and y != 0 and y != len(inp) - 1:
    nx = x + dirs[dir][0]
    ny = y + dirs[dir][1]
    if inp[ny][nx] != "#":
        x, y = nx, ny
        vis.add((x, y))
    else:
        dir = (dir + 1) % 4

obs = 0

for v in vis:
    vvis = set()
    x, y = ix, iy
    dir = 0
    while x != 0 and x != len(inp[0]) - 1 and y != 0 and y != len(inp) - 1:
        nx = x + dirs[dir][0]
        ny = y + dirs[dir][1]
        if inp[ny][nx] != "#" and (nx, ny) != v:
            x, y = nx, ny
            if (x, y, dir) in vvis:
                obs += 1
                break
        else:
            dir = (dir + 1) % 4
        vvis.add((x, y, dir))
print(obs)