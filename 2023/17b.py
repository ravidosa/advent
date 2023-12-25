import heapq
f = open("2023/input-17.txt", "r")
inp = [[int(x) for x in list(i)] for i in f.read().split("\n")[:-1]]
m, n = len(inp), len(inp[0])
dir = {(0, 1), (1, 0), (0, -1), (-1, 0)}
minh = 9 * (m + n)
vis = [(0, (0, 0), (0,0))]
ch = set()
while vis:
    h, pos, dee = heapq.heappop(vis)
    if pos == (m - 1, n - 1):
        minh = min(minh, h)
    if (pos, dee) in ch:
        continue
    ch.add((pos, dee))
    for d in dir-{(dee),(-dee[0], -dee[1])}:
        ne,hh = pos,h
        for k in range(1, 10 + 1):
            ne=(pos[0] + k * d[0], pos[1] + k * d[1])
            if 0 <= ne[0] and ne[0] <= m - 1 and 0 <= ne[1] and ne[1] <= n - 1:
                hh += inp[ne[1]][ne[0]]
                if hh <= minh and k >= 4:
                    heapq.heappush(vis, (hh,ne,d))
    
print(minh)