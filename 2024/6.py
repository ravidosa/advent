from utils import *
inp = open("2024/input-6.txt", "r").read().strip()

grid = Grid(inp)
start = grid.find("^")[0]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

r, c = start
dir = 0
vis = set()
vis.add((r, c))
while 1 <= r < grid.rows - 1 and 1 <= c < grid.cols - 1:
    nr, nc = r + dirs[dir][0], c + dirs[dir][1]
    if grid.grid[nr][nc] != "#":
        r, c = nr, nc
        vis.add((r, c))
    else:
        dir = (dir + 1) % 4
print(len(vis))

obs = 0
for v in vis:
    vvis = set()
    r, c = start
    dir = 0
    while 1 <= r < grid.rows - 1 and 1 <= c < grid.cols - 1:
        nr, nc = r + dirs[dir][0], c + dirs[dir][1]
        if grid.grid[nr][nc] != "#" and (nr, nc) != v:
            r, c = nr, nc
            if (r, c, dir) in vvis:
                obs += 1
                break
        else:
            dir = (dir + 1) % 4
        vvis.add((r, c, dir))
print(obs)