from utils import *
inp = input_file(2024, 12).strip()

grid = Grid(inp)
plants = set(inp) - {"\n"}
regions = []
filled = set()
for p in grid.cells():
    if p not in filled:
        floodfill = list(grid.bfs(p, lambda currv, nextv: currv == nextv))
        regions.append(floodfill)
        filled.update(floodfill)

print(sum(map(lambda r: area(r) * peri(r), regions)))

print(sum(map(lambda r: area(r) * sides(r), regions)))