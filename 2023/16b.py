f = open("2023/input-16.txt", "r")
inp = f.read()[:-1].split("\n")
load = 0
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
refldic = {("/", 0): [3], ("\\", 0): [2], ("-", 0): [2, 3],
("/", 1): [2], ("\\", 1): [3], ("-", 1): [2, 3],
("/", 2): [1], ("\\", 2): [0], ("|", 2): [0, 1],
("/", 3): [0], ("\\", 3): [1], ("|", 3): [0, 1]}
m, n = len(inp[0]), len(inp)
maxeneg = 0
for i in range(m):
    for j in [(0, 0), (n - 1, 1)]:
        vis = set()
        vis.add((i, j[0], j[1]))
        eneg = set()
        while len(vis) > 0:
            pos = list(vis)[0]
            vis = set(list(vis)[1:])
            if 0 <= pos[0] and pos[0] <= n - 1 and 0 <= pos[1] and pos[1] <= m - 1:
                if pos not in eneg:
                    eneg.add(pos)
                    for dd in refldic.get((inp[pos[1]][pos[0]], pos[2]), [pos[2]]):
                        vis.add((pos[0] + dir[dd][0], pos[1] + dir[dd][1], dd))
        maxeneg = max(maxeneg, len(set([(e[0], e[1]) for e in list(eneg)])))
for j in range(n):
    for i in [(0, 2), (m - 1, 3)]:
        vis = set()
        vis.add((i[0], j, i[1]))
        eneg = set()
        while len(vis) > 0:
            pos = list(vis)[0]
            vis = set(list(vis)[1:])
            if 0 <= pos[0] and pos[0] <= n - 1 and 0 <= pos[1] and pos[1] <= m - 1:
                if pos not in eneg:
                    eneg.add(pos)
                    for dd in refldic.get((inp[pos[1]][pos[0]], pos[2]), [pos[2]]):
                        vis.add((pos[0] + dir[dd][0], pos[1] + dir[dd][1], dd))
        maxeneg = max(maxeneg, len(set([(e[0], e[1]) for e in list(eneg)])))
print(maxeneg)