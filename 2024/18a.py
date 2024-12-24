import heapq

f = open("2024/input-18.txt", "r")
inp = [[int(x) for x in i.split(",")] for i in f.read().split("\n")]

N = 70
M = 1024

grid = [["." for __ in range(N + 1)] for _ in range(N + 1)]
for i in inp[:M]:
    grid[i[1]][i[0]] = "#"

s = (0, 0)
e = (N, N)

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

q = [(0, s, 0)]
d = {(s, 0): 0}

while len(q) > 0:
    dis, pos, dirr = heapq.heappop(q)
    x, y = pos
    dx, dy = dirs[dirr]
    if pos == e:
        print(dis)
        break
    if dis > d[(pos, dirr)]:
        continue
    for dd in range(4):
        ddx, ddy = dirs[dd]
        if dx == -ddx and dy == -dy:
            continue
        cost = 1
        if 0 <= x + ddx <= len(grid[0]) - 1 and 0 <= y + ddy <= len(grid) - 1 and grid[y + ddy][x + ddx] != "#":
            if ((x + ddx, y + ddy), dd) not in d or d[((x + ddx, y + ddy), dd)] > dis + cost:
                d[((x + ddx, y + ddy), dd)] = dis + cost
                heapq.heappush(q, (dis + cost, (x + ddx, y + ddy), dd))