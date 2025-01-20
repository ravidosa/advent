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

p1 = sum(p[1] for p in bigcup(part_dict.values()))

p2 = sum(prod(pp[1] for pp in part_dict[p]) for p in part_dict if len(part_dict[p]) == 2 and grid.get_pos(p) == "*")

output(p1, p2)