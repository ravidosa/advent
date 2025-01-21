from utils import *
inp = input_file(2023, 13).strip()

parsed_input = parser(inp.replace(".", "0").replace("#", "1"), ["\n\n"], Grid)

def row_refl(grid, err):
    for r in range(1, grid.rows):
        if sum(grid.get_pos((r - i - 1, c)) != grid.get_pos((r + i, c)) for c in range(grid.cols) for i in range(min(r, grid.rows - r))) == err:
            return r
    return 0
def col_refl(grid, err):
    for c in range(1, grid.cols):
        if sum(grid.get_pos((r, c - i - 1)) != grid.get_pos((r, c + i)) for r in range(grid.rows) for i in range(min(c, grid.cols - c))) == err:
            return c
    return 0

p1 = sum(100 * row_refl(i, 0) + col_refl(i, 0) for i in parsed_input)

p2 = sum(100 * row_refl(i, 1) + col_refl(i, 1) for i in parsed_input)

output(p1, p2)