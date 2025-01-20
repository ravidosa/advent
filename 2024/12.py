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

p1 = sum(map(lambda r: area(r) * peri(r), regions))

p2 = sum(map(lambda r: area(r) * sides(r), regions))

output(p1, p2)