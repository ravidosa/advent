f = open("2024/input-12.txt", "r")
inp = f.read().split("\n")

vis = set()

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

price = 0

for i in range(len(inp[0])):
    for j in range(len(inp)):
        if (i, j) not in vis:
            vissy = set()
            area = 0
            peri = 0
            pos = (i, j)
            vissy.add(pos)
            while len(vissy) > 0:
                pos = vissy.pop()
                x, y = pos
                vis.add(pos)
                area += 1
                if x == 0 or inp[y][x] != inp[y][x - 1]:
                    peri += 1
                if x == len(inp[0]) - 1 or inp[y][x] != inp[y][x + 1]:
                    peri += 1
                if y == 0 or inp[y][x] != inp[y - 1][x]:
                    peri += 1
                if y == len(inp) - 1 or inp[y][x] != inp[y + 1][x]:
                    peri += 1
                for d in dirs:
                    nx, ny = x + d[0], y + d[1]
                    if 0 <= nx <= len(inp[0]) - 1 and 0 <= ny <= len(inp) - 1:
                        npos = (nx, ny)
                        if npos not in vis and inp[y][x] == inp[ny][nx]:
                            vissy.add(npos)
            price += area * peri
print(price)