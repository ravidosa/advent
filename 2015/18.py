from utils import *
inp = open("2015/input-18.txt", "r").read()

parsed_input = inp.replace(".", "0").replace("#", "1")

grid = Grid(parsed_input, int)
for _ in range(100):
    new_grid = [[0 for _ in range(grid.cols)] for __ in range(grid.rows)]
    for r in range(grid.rows):
        for c in range(grid.cols):
            neigh_on = 0
            for dr in [-1, 0, 1]:
                for dc in ([-1, 0, 1] if dr != 0 else [-1, 1]):
                    if 0 <= r + dr < grid.rows and 0 <= c + dc < grid.cols:
                        neigh_on += grid.grid[r + dr][c + dc]
            if (grid.grid[r][c] == 1 and neigh_on in [2, 3]) or (grid.grid[r][c] == 0 and neigh_on in [3]):
                new_grid[r][c] = 1
    grid.grid = new_grid
print(summer(grid.grid))

grid = Grid(parsed_input, int)
for _ in range(100):
    new_grid = [[1 if (r in [0, grid.rows - 1] and c in [0, grid.cols - 1]) else 0 for c in range(grid.cols)] for r in range(grid.rows)]
    for r in range(grid.rows):
        for c in range(grid.cols):
            neigh_on = 0
            for dr in [-1, 0, 1]:
                for dc in ([-1, 0, 1] if dr != 0 else [-1, 1]):
                    if 0 <= r + dr < grid.rows and 0 <= c + dc < grid.cols:
                        neigh_on += grid.grid[r + dr][c + dc]
            if (grid.grid[r][c] == 1 and neigh_on in [2, 3]) or (grid.grid[r][c] == 0 and neigh_on in [3]):
                new_grid[r][c] = 1
    grid.grid = new_grid
print(summer(grid.grid))