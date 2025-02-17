from utils import *
inp = input_file(2019, 3).strip()

parsed_input = parser(inp, "{{ls,}}")

ints = set()
vis = set()
steps = {}
pos = 0+0j
step = 0
for i in parsed_input[0]:
    dir = dir_letter[i[0]]["comp"]
    for i in range(int(i[1:])):
        pos += dir
        step += 1
        vis.add(pos)
        steps[pos] = step
pos = 0+0j
step = 0
for i in parsed_input[1]:
    dir = dir_letter[i[0]]["comp"]
    for i in range(int(i[1:])):
        pos += dir
        step += 1
        if pos in vis:
            ints.add(pos)
            steps[pos] += step

closest_int = min(ints, key=lambda i: abs(int(i.real)) + abs(int(i.imag)))
p1 = abs(int(closest_int.real)) + abs(int(closest_int.imag))

p2 = minval(ints, key=lambda i: steps[i])

output(p1, p2)