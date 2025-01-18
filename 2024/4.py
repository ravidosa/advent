from utils import *
inp = open("2024/input-4.txt", "r").read().strip()

grid = Grid(inp)

s = 0
for pos in grid.cells():
    r, c = pos
    s += functools.reduce(operator.concat, map(lambda i: grid.get_pos((r, c + i)), range(min(4, grid.cols - c))), "") in ["XMAS", "SAMX"]
    s += functools.reduce(operator.concat, map(lambda i: grid.get_pos((r + i, c)), range(min(4, grid.rows - r))), "") in ["XMAS", "SAMX"]
    s += functools.reduce(operator.concat, map(lambda i: grid.get_pos((r + i, c + i)), range(min(4, grid.rows - r, grid.cols - c))), "") in ["XMAS", "SAMX"]
    s += functools.reduce(operator.concat, map(lambda i: grid.get_pos((r + i, c - i)), range(min(4, grid.rows - r, c + 1))), "") in ["XMAS", "SAMX"]
print(s)

s = 0
for r in range(1, grid.rows - 1):
    for c in range(1, grid.cols - 1):
        s += (grid.get_pos((r - 1, c - 1)) + grid.get_pos((r - 1, c + 1)) + grid.get_pos((r, c)) + grid.get_pos((r + 1, c - 1)) + grid.get_pos((r + 1, c + 1))) in ["MSAMS", "SSAMM", "MMASS", "SMASM"]
print(s)