from utils import *
inp = input_file(2015, 18).strip()

parsed_input = inp.replace(".", "0").replace("#", "1")

def next_grid(grid, corner=False):
    new_grid = [[(int(r in [0, grid.rows - 1] and c in [0, grid.cols - 1])) if corner else 0 for r in range(grid.cols)] for c in range(grid.rows)]
    for p in grid.cells():
        neigh_on = sum(grid.get_pos(tupadd(p, d)) if tupadd(p, d) in grid else 0 for d in dir_diag_tup)
        if (grid.get_pos(p) == 1 and neigh_on in [2, 3]) or (grid.get_pos(p) == 0 and neigh_on in [3]):
            new_grid[p[0]][p[1]] = 1
    return new_grid

grid = Grid(parsed_input)
for _ in range(100):
    grid.grid = next_grid(grid)
p1 = summer(grid.grid)

grid = Grid(parsed_input)
for _ in range(100):
    grid.grid = next_grid(grid, True)
p2 = summer(grid.grid)

output(p1, p2)