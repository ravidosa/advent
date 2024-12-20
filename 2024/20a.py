import heapq
f = open("2024/input-20.txt", "r")
inp = f.read().split("\n")

s = ("".join(inp).index("S") % len(inp[0]), "".join(inp).index("S") // len(inp[0]))
e = ("".join(inp).index("E") % len(inp[0]), "".join(inp).index("E") // len(inp[0]))
inp = [list(i) for i in inp]

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

dis = [[len(inp) * len(inp[0]) for _ in range(len(inp[0]))] for __ in range(len(inp))]
dis[s[1]][s[0]] = 0

vis = set()
queue = [s]
while len(queue) > 0:
    pos = queue.pop()
    vis.add(pos)
    x, y = pos
    if pos == e:
        break
    for dd in range(4):
        ddx, ddy = dirs[dd]
        if (x + ddx, y + ddy) in vis:
            continue
        if 0 <= x + ddx <= len(inp[0]) - 1 and 0 <= y + ddy <= len(inp) and inp[y + ddy][x + ddx] != "#":
            dis[y + ddy][x + ddx] = min(dis[y + ddy][x + ddx], dis[y][x] + 1)
            queue.append((x + ddx, y + ddy))
cheat_dic = {}
for p1 in vis:
    for p2 in vis:
        cheat = None
        if p1 != p2:
            if abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) <= 2:
                cheat = abs(dis[p1[1]][p1[0]] - dis[p2[1]][p2[0]]) - (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]))
            if cheat and cheat >= 100:
                cheat_dic[cheat] = cheat_dic.get(cheat, 0) + 1
print(sum(cheat_dic.values()) // 2)