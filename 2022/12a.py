f = open("2022/input-12.txt", "r")
inp = f.read().split("\n")
m, n = len(inp[:-1]), len(inp[0])
S, E = "".join(inp[:-1]).index("S"), "".join(inp[:-1]).index("E")
S, E = (S % n, S // n), (E % n, E // n)
inp[S[1]] = inp[S[1]][:S[0]] + "a" + inp[S[1]][S[0] + 1:]
inp[E[1]] = inp[E[1]][:E[0]] + "z" + inp[E[1]][E[0] + 1:]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dist = [[m * n + 1 for i in range(n)] for i in range(m)]
vis = set([S])
dist[S[1]][S[0]] = 0
while len(vis) > 0:
    pos = list(vis)[0]
    vis = set(list(vis)[1:])
    if pos != E:
        for d in dir:
            ne = (pos[0] + d[0], pos[1] + d[1])
            if 0 <= ne[0] and ne[0] <= n - 1 and 0 <= ne[1] and ne[1] <= m - 1:
                if ord(inp[ne[1]][ne[0]]) - ord(inp[pos[1]][pos[0]]) <= 1 and dist[ne[1]][ne[0]] > dist[pos[1]][pos[0]] + 1:
                    vis.add(ne)
                    dist[ne[1]][ne[0]] = dist[pos[1]][pos[0]] + 1
print(dist[E[1]][E[0]])