from utils import *
inp = open("2021/input-9.txt", "r").read().strip()

grid = Grid(inp)
low_points = list(filter(lambda p: all(map(lambda d: grid.get_pos(tupadd(p, d)) > grid.get_pos(p) if tupadd(p, d) in grid else True, grid.dirs)), grid.cells()))

print(sum(map(lambda p: 1 + grid.get_pos(p), low_points)))

regions = []
filled = set()
for p in low_points:
    floodfill = list(grid.bfs(p, lambda currv, nextv: currv < nextv and nextv != 9))
    regions.append(floodfill)
    filled.update(floodfill)
regions = sorted(regions, key=len, reverse=True)
print(prod(map(lambda i: len(regions[i]), range(3))))