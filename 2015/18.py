from utils import *
inp = input_file(2015, 18).strip()

parsed_input = inp.replace(".", "0").replace("#", "1")

grid = Grid(parsed_input)
for _ in range(100):
    new_grid = [[0 for _ in range(grid.cols)] for __ in range(grid.rows)]
    for p in grid.cells():
        neigh_on = sum(map(lambda d: grid.get_pos(tupadd(p, d)) if tupadd(p, d) in grid else 0, dir_diag_tup))
        if (grid.get_pos(p) == 1 and neigh_on in [2, 3]) or (grid.get_pos(p) == 0 and neigh_on in [3]):
            new_grid[p[0]][p[1]] = 1
    grid.grid = new_grid
print(summer(grid.grid))

grid = Grid(parsed_input)
for _ in range(100):
    new_grid = [[(int(r in [0, grid.rows - 1] and c in [0, grid.cols - 1])) for c in range(grid.cols)] for r in range(grid.rows)]
    for p in grid.cells():
        neigh_on = sum(map(lambda d: grid.get_pos(tupadd(p, d)) if tupadd(p, d) in grid else 0, dir_diag_tup))
        if (grid.get_pos(p) == 1 and neigh_on in [2, 3]) or (grid.get_pos(p) == 0 and neigh_on in [3]):
            new_grid[p[0]][p[1]] = 1
    grid.grid = new_grid
print(summer(grid.grid))