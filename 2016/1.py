from utils import *
inp = input_file(2016, 1).strip()

parsed_input = parser(inp, "{{ls, }}")

pos, dir = 0+0j, 0+1j
for i in parsed_input:
    dir *= (0+1j if i[0] == "L" else 0-1j)
    pos += int(i[1:]) * dir
p1 = abs(int(pos.real)) + abs(int(pos.imag))

vis = set()
pos, dir = 0+0j, 0+1j
vis.add(pos)
for i in parsed_input:
    dir *= (0+1j if i[0] == "L" else 0-1j)
    rep = False
    for i in range(int(i[1:])):
        pos += dir
        if pos in vis:
            rep = True
            break
        else:
            vis.add(pos)
    if rep:
        break
p2 = abs(int(pos.real)) + abs(int(pos.imag))

output(p1, p2)