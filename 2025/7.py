from utils import *
inp = input_file(2025, 7).strip()

parsed_input = inp

grid = Grid(parsed_input)
S = grid.find("S")[0]
splitters = grid.find("^")

tot = 0
beams = set([S[1]])
for r in range(1, grid.rows):
    beams, beams_ = set(), beams.copy()
    for c in beams_:
        if grid.get_pos((r, c)) == "^":
            tot += 1
            if c > 0:
                beams.add(c - 1)
            if c < grid.cols - 1:
                beams.add(c + 1)
        else:
            beams.add(c)
p1 = tot

paths = {S[1]: 1}
for r in range(1, grid.rows):
    paths, paths_ = {}, paths.copy()
    for c in paths_:
        if grid.get_pos((r, c)) == "^":
            if c > 0:
                paths[c - 1] = paths.get(c - 1, 0) + paths_[c]
            if c < grid.cols - 1:
                paths[c + 1] = paths.get(c + 1, 0) + paths_[c]
        else:
            paths[c] = paths.get(c, 0) + paths_[c]
p2 = sum(paths.values())

output(p1, p2)