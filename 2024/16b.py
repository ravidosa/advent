import heapq

f = open("2024/input-16.txt", "r")
inp = f.read().split("\n")

s = ("".join(inp).index("S") % len(inp[0]), "".join(inp).index("S") // len(inp[0]))
e = ("".join(inp).index("E") % len(inp[0]), "".join(inp).index("E") // len(inp[0]))
inp = [list(i) for i in inp]

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

q = [(0, s, 0)]
d = {(s, 0): 0}
p = {(s, 0): []}

while len(q) > 0:
    dis, pos, dirr = heapq.heappop(q)
    x, y = pos
    dx, dy = dirs[dirr]
    if pos == e:
        sss = set([(pos, dirr)])
        while True:
            u = set(pp for ss in sss for pp in p[ss])
            if u.issubset(sss):
                break
            sss.update(u)
        print(len(set([ss[0] for ss in sss])))
        break
    if dis > d[(pos, dirr)]:
        continue
    for dd in range(4):
        ddx, ddy = dirs[dd]
        if dx == -ddx and dy == -dy:
            continue
        cost = 1 + 1000 * (dx != ddx or dy != ddy)
        if inp[y + ddy][x + ddx] != "#":
            if ((x + ddx, y + ddy), dd) not in d or d[((x + ddx, y + ddy), dd)] > dis + cost:
                d[((x + ddx, y + ddy), dd)] = dis + cost
                p[((x + ddx, y + ddy), dd)] = [((x, y), dirr)]
                heapq.heappush(q, (dis + cost, (x + ddx, y + ddy), dd))
            elif d[((x + ddx, y + ddy), dd)] == dis + cost:
                p[((x + ddx, y + ddy), dd)].append(((x, y), dirr))