import numpy as np
f = open("2022/input-8.txt", "r")
inp = f.read().split("\n")
tr = np.array([[int(t) for t in list(i)] for i in inp[:-1]]).astype(int)
scen = 0
for i in range(1,  len(tr) - 1):
    for j in range(1, len(tr[0]) - 1):
        vis = [np.flip(tr[i, :j:])>=tr[i, j], tr[i, j + 1:]>=tr[i, j], np.flip(tr[:i:, j])>=tr[i, j], tr[i + 1:, j]>=tr[i, j]]
        scen = max(scen, (np.argmax(vis[0]) + 1 if np.max(vis[0]) != 0 else j) * (np.argmax(vis[1]) + 1 if np.max(vis[1]) != 0 else len(tr[0]) - j - 1) * (np.argmax(vis[2]) + 1 if np.max(vis[2]) != 0 else i) * (np.argmax(vis[3]) + 1 if np.max(vis[3]) != 0 else len(tr) - i - 1))
print(scen)