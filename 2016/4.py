from utils import *
inp = input_file(2016, 4).strip()

parsed_input = parser(inp, "{{le-}}[{{s}}]")

real = lambda room: room[0][-1] * ("".join(sorted(lower, key=lambda l: -("".join(room[0][:-1]).count(l))))[:5] == room[1])
p1 = sum(map(real, parsed_input))

for i in parsed_input:
    if "north" in "".join(lower[(lower.index(l) + i[0][-1]) % 26] if l != " " else l for l in " ".join(i[0][:-1])):
        break
p2 = i[0][-1]

output(p1, p2)