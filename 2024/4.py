from utils import *
inp = open("2024/input-4.txt", "r").read().strip()

grid = Grid(inp)

s = 0
for pos in grid.cells():
    s += functools.reduce(operator.concat, grid.row(pos, 4)) in ["XMAS", "SAMX"]
    s += functools.reduce(operator.concat, grid.col(pos, 4), "") in ["XMAS", "SAMX"]
    s += functools.reduce(operator.concat, grid.pdiag(pos, 4), "") in ["XMAS", "SAMX"]
    s += functools.reduce(operator.concat, grid.ndiag(pos, 4), "") in ["XMAS", "SAMX"]
print(s)

s = 0
for r in range(1, grid.rows - 1):
    for c in range(1, grid.cols - 1):
        s += (grid.get_pos((r - 1, c - 1)) + grid.get_pos((r - 1, c + 1)) + grid.get_pos((r, c)) + grid.get_pos((r + 1, c - 1)) + grid.get_pos((r + 1, c + 1))) in ["MSAMS", "SSAMM", "MMASS", "SMASM"]
print(s)