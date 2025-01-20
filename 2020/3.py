from utils import *
inp = input_file(2020, 3).strip()

parsed_input = inp.replace(".", "0").replace("#", "1")

grid = Grid(parsed_input, wrap=True)
p1 = sum(grid.get_pos((r, 3 * r)) for r in range(grid.rows))

slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
p2 = prod(sum(grid.get_pos((sr * r, sc * r)) for r in range(grid.rows // sr)) for sr, sc in slopes)

output(p1, p2)