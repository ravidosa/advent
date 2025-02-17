from utils import *
from intcode import *
inp = input_file(2019, 11).strip()

parsed_input = parser(inp, "{{li,}}")

paint = {}
pos, dir = 0+0j, 0+1j
program = parsed_input.copy()
intc = Computer(program, [0])
execution = intc.run()
while True:
    try:
        next(execution)
        out = intc.pop_out()
        paint[pos] = out[0]
        dir *= (0+1j if out[1] == 0 else 0-1j)
        pos += dir
        intc.push_in([paint.get(pos, 0)])
    except StopIteration:
        break
p1 = len(paint)

paint = {0+0j: 1}
pos, dir = 0+0j, 0+1j
program = parsed_input.copy()
intc = Computer(program, [1])
execution = intc.run()
while True:
    try:
        next(execution)
        out = intc.pop_out()
        paint[pos] = out[0]
        dir *= (0+1j if out[1] == 0 else 0-1j)
        pos += dir
        intc.push_in([paint.get(pos, 0)])
    except StopIteration:
        break
minx, maxx, miny, maxy = int(minval(paint, lambda p: p.real)), int(maxval(paint, lambda p: p.real)), int(minval(paint, lambda p: p.imag)), int(maxval(paint, lambda p: p.imag))
disp = ""
for y in range(maxy, miny - 1, -1):
    for x in range(minx, maxx + 1):
        disp += ("##" if paint.get(x + y * 1j, 0) else "  ")
    disp += "\n"
p2 = disp

output(p1, p2)