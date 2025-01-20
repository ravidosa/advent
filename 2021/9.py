from utils import *
inp = input_file(2021, 9).strip()

grid = Grid(inp)
low_points = [p for p in grid.cells() if all(grid.get_pos(tupadd(p, d)) > grid.get_pos(p) if tupadd(p, d) in grid else True for d in grid.dirs)]

p1 = sum(1 + grid.get_pos(p) for p in low_points)

regions = []
filled = set()
for p in low_points:
    floodfill = list(grid.bfs(p, lambda currv, nextv: currv < nextv and nextv != 9))
    regions.append(floodfill)
    filled.update(floodfill)
regions = sorted(regions, key=len, reverse=True)
p2 = prod(len(regions[i]) for i in range(3))

output(p1, p2)