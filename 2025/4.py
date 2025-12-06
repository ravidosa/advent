from utils import *
inp = input_file(2025, 4).strip()

parsed_input = inp

def forklift(grid):
    grid_ = Grid(repr(grid))
    rem = 0
    for r in range(grid.rows):
        for c in range(grid.cols):
            if grid.get_pos((r, c)) == "@":
                neighs = [grid_.get_pos((r + i, c + j)) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0) and grid.get_pos((r + i, c + j)) == "@"]
                rem += len(neighs) < 4
                grid_.set_pos((r, c), "." if len(neighs) < 4 else "@")
    return grid_, rem

tot = 0
grid = Grid(parsed_input)
grid, rem = forklift(grid)
p1 = rem

tot = 0
rem = 420
grid = Grid(parsed_input)
while rem > 0:
    grid, rem = forklift(grid)
    tot += rem
p2 = tot

output(p1, p2)