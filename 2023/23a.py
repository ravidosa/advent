import sys
sys.setrecursionlimit(10000)
f = open("2023/input-23.txt", "r")
inp = f.read().split("\n")[:-1]
m, n = len(inp), len(inp[0])
def neb(pos):
    if inp[pos[1]][pos[0]] == ">":
        return [(pos[0] + 1, pos[1])]
    elif inp[pos[1]][pos[0]] == "<":
        return [(pos[0] - 1, pos[1])]
    elif inp[pos[1]][pos[0]] == "^":
        return [(pos[0], pos[1] - 1)]
    elif inp[pos[1]][pos[0]] == "v":
        return [(pos[0], pos[1] + 1)]
    elif inp[pos[1]][pos[0]] == ".":
        nene = [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]
        return [ne for ne in nene if 0 <= ne[0] and ne[0] <= n - 1 and 0 <= ne[1] and ne[1] <= m - 1 and inp[ne[1]][ne[0]] != "#"]
    else:
        return []

def dfs(pos, d, ch):
    if pos == (n - 2, m - 1):
        yield d
    for ne in neb(pos):
        if ne not in ch:
            ch.add(ne)
            yield from dfs(ne, d + 1, ch)
            ch.remove(ne)

print(max(dfs((1, 0), 0, {(1, 0)})))