from utils import *
inp = input_file(2021, 5).strip()

parsed_input = parser(inp, ["\n", " -> |,"])

grid = {}
for i in parsed_input:
    x1, y1, x2, y2 = i
    if (x1 == x2):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[(x1, y)] = grid.get((x1, y), 0) + 1
    elif (y1 == y2):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            grid[(x, y1)] = grid.get((x, y1), 0) + 1
p1 = sum(map(lambda p: grid[p] >= 2, grid))

for i in parsed_input:
    x1, y1, x2, y2 = i
    if (x1 != x2 and y1 != y2):
        for i in range(abs(x2 - x1) + 1):
            x, y = x1 + i * (1 if x2 > x1 else -1 if x2 < x1 else 0), y1 + i * (1 if y2 > y1 else -1 if y2 < y1 else 0)
            grid[(x, y)] = grid.get((x, y), 0) + 1
p2 = sum(map(lambda p: grid[p] >= 2, grid))

output(p1, p2)