from utils import *
inp = open("2022/input-8.txt", "r").read().strip()

grid = Grid(inp)

visible = lambda pos: (r := pos[0]) in [0, grid.rows - 1] or (c := pos[1]) in [0, grid.cols - 1] or grid.get_pos(pos) > max(grid.row((r, c + 1))) or grid.get_pos(pos) > max(grid.row((r, 0), c)) or grid.get_pos(pos) > max(grid.col((r + 1, c))) or grid.get_pos(pos) > max(grid.col((0, c), r))
print(sum(map(visible, grid.cells())))

def scenic(pos):
    r, c = pos
    scen = 1
    row_e = grid.row((r, c + 1))
    scen *= (0 if len(row_e) == 0 else argmax(map(lambda ind: int(row_e[ind] >= grid.get_pos(pos)), range(len(row_e)))) + 1 if max(row_e) >= grid.get_pos(pos) else grid.cols - c - 1)
    row_w = grid.row((r, 0), c)[::-1]
    scen *= (0 if len(row_w) == 0 else argmax(map(lambda ind: int(row_w[ind] >= grid.get_pos(pos)), range(len(row_w)))) + 1 if max(row_w) >= grid.get_pos(pos) else c)
    col_s = grid.col((r + 1, c))
    scen *= (0 if len(col_s) == 0 else argmax(map(lambda ind: int(col_s[ind] >= grid.get_pos(pos)), range(len(col_s)))) + 1 if max(col_s) >= grid.get_pos(pos) else grid.rows - r - 1)
    col_n = grid.col((0, c), r)[::-1]
    scen *= (0 if len(col_n) == 0 else argmax(map(lambda ind: int(col_n[ind] >= grid.get_pos(pos)), range(len(col_n)))) + 1 if max(col_n) >= grid.get_pos(pos) else r)
    return scen
print(maxval(grid.cells(), key=scenic))