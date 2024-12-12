f = open("2024/input-12.txt", "r")
inp = f.read().split("\n")

vis = set()

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

price = 0

for i in range(len(inp[0])):
    for j in range(len(inp)):
        if (i, j) not in vis:
            vissy = set()
            vissy2 = set()
            area = 0
            sides = 0
            pos = (i, j)
            vissy.add(pos)
            vissy2.add(pos)
            while len(vissy) > 0:
                pos = vissy.pop()
                x, y = pos
                vis.add(pos)
                vissy2.add(pos)
                area += 1
                for d in dirs:
                    nx, ny = x + d[0], y + d[1]
                    if 0 <= nx <= len(inp[0]) - 1 and 0 <= ny <= len(inp) - 1 and inp[y][x] == inp[ny][nx]:
                        npos = (nx, ny)
                        if npos not in vis:
                            vissy.add(npos)
            for v in vissy2:
                x, y = v
                sides += (x - 1, y) not in vissy2 and (x, y - 1) not in vissy2
                sides += (x + 1, y) not in vissy2 and (x, y - 1) not in vissy2
                sides += (x - 1, y) not in vissy2 and (x, y + 1) not in vissy2
                sides += (x + 1, y) not in vissy2 and (x, y + 1) not in vissy2
                sides += (x - 1, y) in vissy2 and (x, y - 1) in vissy2 and (x - 1, y - 1) not in vissy2
                sides += (x + 1, y) in vissy2 and (x, y - 1) in vissy2 and (x + 1, y - 1) not in vissy2
                sides += (x - 1, y) in vissy2 and (x, y + 1) in vissy2 and (x - 1, y + 1) not in vissy2
                sides += (x + 1, y) in vissy2 and (x, y + 1) in vissy2 and (x + 1, y + 1) not in vissy2
            price += area * sides
print(price)