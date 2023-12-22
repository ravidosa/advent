import numpy as np
f = open("2022/input-8.txt", "r")
inp = f.read().split("\n")
tr = np.array([[int(t) for t in list(i)] for i in inp[:-1]]).astype(int)
vis = [[1 for t in row] for row in tr]
for i in range(1,  len(vis) - 1):
    for j in range(1, len(vis[0]) - 1):
        vis[i][j] = int((tr[i, j] > max(tr[i, :j])) or (tr[i, j] > max(tr[i, j + 1:])) or (tr[i, j] > max(tr[:i, j])) or (tr[i, j] > max(tr[i + 1:, j])))
print(sum([row.count(1) for row in vis]))