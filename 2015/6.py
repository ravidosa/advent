from utils import *
inp = open("2015/input-6.txt", "r").read()

parsed_input = parser(inp, ["\n", r"turn| through | |,"])

lights = [[0 for _ in range(1000)] for _ in range(1000)]
for inp in parsed_input:
    instr, ix, iy, fx, fy = inp
    for x in range(ix, fx + 1):
        for y in range(iy, fy + 1):
            if instr == "on":
                lights[y][x] = 1
            if instr == "off":
                lights[y][x] = 0
            if instr == "toggle":
                lights[y][x] = 1 - lights[y][x]
print(summer(lights))

lights = [[0 for _ in range(1000)] for _ in range(1000)]
for inp in parsed_input:
    instr, ix, iy, fx, fy = inp
    for x in range(ix, fx + 1):
        for y in range(iy, fy + 1):
            if instr == "on":
                lights[y][x] += 1
            if instr == "off":
                lights[y][x] = max(lights[y][x] - 1, 0)
            if instr == "toggle":
                lights[y][x] += 2
print(summer(lights))