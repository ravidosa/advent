f = open("2023/input-10.txt", "r")
inp = f.read().split("\n")
m, n = len(inp[:-1]), len(inp[0])
S = "".join(inp[:-1]).index("S")
S = (S % n, S // n)
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
ch = ["|LJ", "|7F", "-J7", "-LF"]
chd = {"-": [2, 3], "|": [0, 1], "7": [0, 3], "F": [0, 2], "L": [1, 2], "J": [1, 3]}
dist = [[-1 for j in range(n)] for i in range(m)]
vis = set()
dist[S[1]][S[0]] = 0
for ind, d in enumerate(dir):
    ne = (S[0] + d[0], S[1] + d[1])
    if 0 <= ne[0] and ne[0] <= n - 1 and 0 <= ne[1] and ne[1] <= m - 1 and inp[ne[1]][ne[0]] in ch[ind]:
        vis.add(ne)
        dist[ne[1]][ne[0]] = 1
while len(vis) > 0:
    pos = list(vis)[0]
    vis = set(list(vis)[1:])
    if pos != S:
        for ind, d in enumerate(dir):
            ne = (pos[0] + d[0], pos[1] + d[1])
            if 0 <= ne[0] and ne[0] <= n - 1 and 0 <= ne[1] and ne[1] <= m - 1:
                if ind in chd[inp[pos[1]][pos[0]]] and inp[ne[1]][ne[0]] in ch[ind] and (dist[ne[1]][ne[0]] == -1 or dist[ne[1]][ne[0]] > dist[pos[1]][pos[0]] + 1):
                    vis.add(ne)
                    dist[ne[1]][ne[0]] = dist[pos[1]][pos[0]] + 1
ddist = [[("x" if inp[i][ii] in "|LJ" else "y") if dd >= 0 else " " for ii, dd in enumerate(d)] for i, d in enumerate(dist)]
print(sum([sum([1 if dd == " " and d[:ii].count("x") % 2 == 1 and d[ii+1:].count("x") % 2 == 1 else 0 for ii, dd in enumerate(d)]) for d in ddist]))