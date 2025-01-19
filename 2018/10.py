from utils import *
inp = input_file(2018, 10).strip()

parsed_input = parser(inp, ["\n", "position=<|> velocity=<|>", ", *"])

def bounding(pos):
    minx = minval(pos, key=lambda i: i[0])
    maxx = maxval(pos, key=lambda i: i[0])
    miny = minval(pos, key=lambda i: i[1])
    maxy = maxval(pos, key=lambda i: i[1])
    return minx, maxx, miny, maxy
def cohesion(t):
    newp = list(map(lambda pair: (pair[0][0] + pair[1][0] * t, pair[0][1] + pair[1][1] * t), parsed_input))
    minx, maxx, miny, maxy = bounding(newp)
    return (maxx - minx) + (maxy - miny)
mint = min(range(20000), key=cohesion)

newp = list(map(lambda pair: (pair[0][0] + pair[1][0] * mint, pair[0][1] + pair[1][1] * mint), parsed_input))
minx, maxx, miny, maxy = bounding(newp)
grid = Grid((" " * (maxx - minx + 1) + "\n") * (maxy - miny + 1))
for p in newp:
    r, c = p[1] - miny, p[0] - minx
    grid.set_pos((r, c), "#")
p1 = grid

p2 = mint

output(p1, p2)