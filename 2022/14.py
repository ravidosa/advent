from utils import *
inp = input_file(2022, 14).strip()

parsed_input = parser(inp, ["\n", " -> ", ","], eval)

maxy = max(maxval(i, key=lambda j: j[1]) for i in parsed_input) + 2
maxx = 2 * maxy + 1
grid = Grid(("." * maxx + "\n") * maxy)
for i in parsed_input:
    for pair in zip(i[:-1], i[1:]):
        for r in range(minval(pair, key=lambda i: i[1]), maxval(pair, key=lambda i: i[1]) + 1):
            for c in range(minval(pair, key=lambda i: i[0]) - (500 - maxy), maxval(pair, key=lambda i: i[0]) - (500 - maxy) + 1):
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