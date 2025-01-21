from utils import *
inp = input_file(2023, 11).strip()

parsed_input = inp.replace(".", "0").replace("#", "1")

grid = Grid(parsed_input)
gals = grid.find(1)
empr = [r for r in range(grid.rows) if sum(grid.row((r, 0))) == 0]
empc = [c for c in range(grid.cols) if sum(grid.col((0, c))) == 0]
dist = lambda g1, g2, exp: manhattan(g1, g2) + (exp - 1) * (sum(min(g1[0], g2[0]) < r < max(g1[0], g2[0]) for r in empr) + sum(min(g1[1], g2[1]) < c < max(g1[1], g2[1]) for c in empc))

p1 = sum(dist(g1, g2, 2) for g1, g2 in itertools.combinations(gals, 2))

p2 = sum(dist(g1, g2, 1000000) for g1, g2 in itertools.combinations(gals, 2))

output(p1, p2)