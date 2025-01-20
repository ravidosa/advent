from utils import *
inp = input_file(2021, 9).strip()

grid = Grid(inp)
low_points = [p for p in grid.cells() if all(map(lambda d: grid.get_pos(tupadd(p, d)) > grid.get_pos(p) if tupadd(p, d) in grid else True, grid.dirs))]

p1 = sum(map(lambda p: 1 + grid.get_pos(p), low_points))

regions = []
filled = set()
for p in low_points:
    floodfill = list(grid.bfs(p, lambda currv, nextv: currv < nextv and nextv != 9))
    regions.append(floodfill)
    filled.update(floodfill)
regions = sorted(regions, key=len, reverse=True)
p2 = prod(map(lambda i: len(regions[i]), range(3)))

output(p1, p2)