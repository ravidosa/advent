from utils import *
from intcode import *
inp = input_file(2019, 13).strip()

parsed_input = parser(inp, "{{li,}}")

tiles = {}
program = parsed_input.copy()
intc = Computer(program, [])
all(intc.run())
out = intc.pop_out()
tiles = {x + y * 1j: t for x, y, t in zip(out[::3], out[1::3], out[2::3])} 
p1 = operator.countOf(tiles.values(), 2)
minx, maxx, miny, maxy = int(minval(tiles, lambda p: p.real)), int(maxval(tiles, lambda p: p.real)), int(minval(tiles, lambda p: p.imag)), int(maxval(tiles, lambda p: p.imag))

tiles = {}
program = parsed_input.copy()
intc = Computer(program, [0,1])
intc[0] = 2
execution = intc.run()
draw = {0: " ", 1: "#", 2: "B", 3: "P", 4: "O"}
while True:
    try:
        next(execution)
        out = intc.pop_out()
        tiles.update({x + y * 1j: t for x, y, t in zip(out[::3], out[1::3], out[2::3])})
        p, b = keyval(tiles, 3)[0], keyval(tiles, 4)[0]
        intc.push_in([-1 if p.real > b.real else 1 if p.real < b.real else 0])
    except StopIteration:
        break
p2 = intc.pop_out()[-1]

output(p1, p2)