from utils import *
inp = input_file(2023, 3).strip()

grid = Grid(inp, str)
part_dict = {}
for r in range(grid.rows):
    c = 0
    while c < grid.cols:
        l = 1
        if grid.get_pos((r, c)).isdigit():
            while c + l <= grid.cols and grid.get_pos((r, c + l - 1)).isdigit():
                l += 1
            for chc, chr in itertools.product(range(max(0, c - 1), min(grid.cols, c + l)), range(max(0, r - 1), min(grid.rows, r + 2))):
                if grid.get_pos((chr, chc)) in "`~!@#$%^&*()_-+=[]{}\\|;:,<>/?":
                    part_dict[(chr, chc)] = part_dict.get((chr, chc), set()).union({((r, c, l), int("".join(grid.row((r, c), l - 1))))})
                    break
        c += l

p1 = sum(map(lambda p: p[1], set().union(*part_dict.values())))

p2 = sum(map(lambda p: prod(map(lambda pp: pp[1], part_dict[p])) * (len(part_dict[p]) == 2) * (grid.get_pos(p) == "*"), part_dict))

output(p1, p2)