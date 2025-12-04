from utils import *
inp = input_file(2025, 4).strip()

parsed_input = inp

tot = 0
grid = Grid(parsed_input)
for r in range(grid.rows):
    for c in range(grid.cols):
        if grid.get_pos((r, c)) == "@":
            neighs = [grid.get_pos((r + i, c + j)) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0) and grid.get_pos((r + i, c + j)) == "@"]
            tot += len(neighs) < 4
p1 = tot

rem = 0
tot = 420
grid = Grid(parsed_input)
while tot > 0:
    tot = 0
    for r in range(grid.rows):
        for c in range(grid.cols):
            if grid.get_pos((r, c)) == "@":
                neighs = [grid.get_pos((r + i, c + j)) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0) and grid.get_pos((r + i, c + j)) == "@"]
                tot += len(neighs) < 4
                grid.set_pos((r, c), "." if len(neighs) < 4 else "@")
    rem += tot
p2 = rem

output(p1, p2)