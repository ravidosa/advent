from utils import *
inp = open("2024/input-4.txt", "r").read().strip()

grid = Grid(inp)

s = 0
for r in range(grid.rows):
    for c in range(grid.cols):
        s += functools.reduce(operator.concat, map(lambda i: grid.grid[r][c + i], range(min(4, grid.cols - c))), "") in ["XMAS", "SAMX"]
        s += functools.reduce(operator.concat, map(lambda i: grid.grid[r + i][c], range(min(4, grid.rows - r))), "") in ["XMAS", "SAMX"]
        s += functools.reduce(operator.concat, map(lambda i: grid.grid[r + i][c + i], range(min(4, grid.rows - r, grid.cols - c))), "") in ["XMAS", "SAMX"]
        s += functools.reduce(operator.concat, map(lambda i: grid.grid[r + i][c - i], range(min(4, grid.rows - r, c + 1))), "") in ["XMAS", "SAMX"]
print(s)

s = 0
for r in range(1, grid.rows - 1):
    for c in range(1, grid.cols - 1):
        s += (grid.grid[r - 1][c - 1] + grid.grid[r - 1][c + 1] + grid.grid[r][c] + grid.grid[r + 1][c - 1] + grid.grid[r + 1][c + 1]) in ["MSAMS", "SSAMM", "MMASS", "SMASM"]
print(s)