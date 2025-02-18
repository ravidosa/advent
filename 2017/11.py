from utils import *
inp = input_file(2017, 11).strip()

parsed_input = parser(inp, "{{ls,}}")

dir_map = {"n": 0+1j, "s": 0-1j, "ne": 1+1j, "nw": -1+0j, "se": 1+0j, "sw": -1-1j}
dist = lambda p: int(max(abs(p.real), abs(p.imag))) if p.real * p.imag > 0 else int(abs(p.real) + abs(p.imag))

posl = []
pos = 0+0j
for i in parsed_input:
    pos = pos + dir_map[i]
    posl.append(pos)

p1 = dist(posl[-1])

p2 = maxval(posl, key=dist)

output(p1, p2)
