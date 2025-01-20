from utils import *
inp = input_file(2022, 8).strip()

grid = Grid(inp)

visible = lambda pos: (r := pos[0]) in [0, grid.rows - 1] or (c := pos[1]) in [0, grid.cols - 1] or grid.get_pos(pos) > max(grid.row((r, c + 1))) or grid.get_pos(pos) > max(grid.row((r, 0), c)) or grid.get_pos(pos) > max(grid.col((r + 1, c))) or grid.get_pos(pos) > max(grid.col((0, c), r))
p1 = sum(map(visible, grid.cells()))

def scenic(pos):
    r, c = pos
    if r in [0, grid.rows - 1] or c in [0, grid.cols - 1]:
        return 0
    scen = 1
    row_e = grid.row((r, c + 1))
    scen *= (argmax(map(lambda ind: int(row_e[ind] >= grid.get_pos(pos)), range(len(row_e)))) + 1 if max(row_e) >= grid.get_pos(pos) else grid.cols - c - 1)
    row_w = grid.row((r, 0), c)[::-1]
    scen *= (argmax(map(lambda ind: int(row_w[ind] >= grid.get_pos(pos)), range(len(row_w)))) + 1 if max(row_w) >= grid.get_pos(pos) else c)
    col_s = grid.col((r + 1, c))
    scen *= (argmax(map(lambda ind: int(col_s[ind] >= grid.get_pos(pos)), range(len(col_s)))) + 1 if max(col_s) >= grid.get_pos(pos) else grid.rows - r - 1)
    col_n = grid.col((0, c), r)[::-1]
    scen *= (argmax(map(lambda ind: int(col_n[ind] >= grid.get_pos(pos)), range(len(col_n)))) + 1 if max(col_n) >= grid.get_pos(pos) else r)
    return scen
p2 = maxval(grid.cells(), key=scenic)

output(p1, p2)