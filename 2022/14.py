from utils import *
inp = input_file(2022, 14).strip()

parsed_input = parser(inp, ["\n", " -> ", ","], eval)

maxy = max(maxval(i, key=lambda j: j[1]) for i in parsed_input) + 2
maxx = 2 * maxy + 1
grid = Grid(("." * maxx + "\n") * maxy)
for i in parsed_input:
    for p1, p2 in zip(i[:-1], i[1:]):
        for r in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
            for c in range(min(p1[0], p2[0]) - (500 - maxy), max(p1[0], p2[0]) - (500 - maxy) + 1):
                grid.set_pos((r, c), "#")

s = 0
currp = (0, maxy)
while currp[0] != maxy - 1:
    if grid.get_pos(tupadd(currp, (1, 0))) == "#":
        if grid.get_pos(tupadd(currp, (1, -1))) == "#":
            if grid.get_pos(tupadd(currp, (1, 1))) == "#":
                s += 1
                grid.set_pos(currp, "#")
                currp = (0, maxy)
            else:
                currp = tupadd(currp, (1, 1))
        else:
            currp = tupadd(currp, (1, -1))
    else:
        currp = tupadd(currp, (1, 0))
p1 = s

currp = (0, maxy)
while grid.get_pos((0, maxy)) != "#":
    if currp[0] == maxy - 1:
        s += 1
        grid.set_pos(currp, "#")
        currp = (0, maxy)
    else:
        if grid.get_pos(tupadd(currp, (1, 0))) == "#":
            if grid.get_pos(tupadd(currp, (1, -1))) == "#":
                if grid.get_pos(tupadd(currp, (1, 1))) == "#":
                    s += 1
                    grid.set_pos(currp, "#")
                    currp = (0, maxy)
                else:
                    currp = tupadd(currp, (1, 1))
            else:
                currp = tupadd(currp, (1, -1))
        else:
            currp = tupadd(currp, (1, 0))
p2 = s

output(p1, p2)