from utils import *
inp = input_file(2015, 6).strip()

parsed_input = parser(inp, ["\n", r"turn| through | |,"])

lights = [[0 for _ in range(1000)] for _ in range(1000)]
for i in parsed_input:
    instr, ix, iy, fx, fy = i
    for x in range(ix, fx + 1):
        for y in range(iy, fy + 1):
            if instr == "on":
                lights[y][x] = 1
            if instr == "off":
                lights[y][x] = 0
            if instr == "toggle":
                lights[y][x] = 1 - lights[y][x]
p1 = summer(lights)

lights = [[0 for _ in range(1000)] for _ in range(1000)]
for i in parsed_input:
    instr, ix, iy, fx, fy = i
    for x in range(ix, fx + 1):
        for y in range(iy, fy + 1):
            if instr == "on":
                lights[y][x] += 1
            if instr == "off":
                lights[y][x] = max(lights[y][x] - 1, 0)
            if instr == "toggle":
                lights[y][x] += 2
p2 = summer(lights)

output(p1, p2)