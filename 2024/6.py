from utils import *
inp = input_file(2024, 6).strip()

grid = Grid(inp)
start = grid.find("^")[0]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
currp = start
dir = 0
vis = set()
vis.add(currp)
while 1 <= currp[0] < grid.rows - 1 and 1 <= currp[1] < grid.cols - 1:
    nextp = tupadd(currp, dirs[dir])
    if grid.get_pos(nextp) != "#":
        currp = nextp
        vis.add(nextp)
    else:
        dir = (dir + 1) % 4
print(len(vis))

obs = 0
for v in vis:
    dir = 0
    vvis = set()
    currp = start
    while 1 <= currp[0] < grid.rows - 1 and 1 <= currp[1] < grid.cols - 1:
        nextp = tupadd(currp, dirs[dir])
        if grid.get_pos(nextp) != "#" and nextp != v:
            currp = nextp
            if (currp, dir) in vvis:
                obs += 1
                break
        else:
            dir = (dir + 1) % 4
        vvis.add((currp, dir))
print(obs)