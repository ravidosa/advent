from utils import *
inp = input_file(2024, 4).strip()

grid = Grid(inp)

s = 0
for pos in grid.cells():
    s += functools.reduce(operator.concat, grid.row(pos, 4), "") in ["XMAS", "SAMX"]
    s += functools.reduce(operator.concat, grid.col(pos, 4), "") in ["XMAS", "SAMX"]
    s += functools.reduce(operator.concat, grid.pdiag(pos, 4), "") in ["XMAS", "SAMX"]
    s += functools.reduce(operator.concat, grid.ndiag(pos, 4), "") in ["XMAS", "SAMX"]
p1 = s

s = 0
for r in range(1, grid.rows - 1):
    for c in range(1, grid.cols - 1):
        s += (grid.get_pos((r - 1, c - 1)) + grid.get_pos((r - 1, c + 1)) + grid.get_pos((r, c)) + grid.get_pos((r + 1, c - 1)) + grid.get_pos((r + 1, c + 1))) in ["MSAMS", "SSAMM", "MMASS", "SMASM"]
p2 = s

output(p1, p2)