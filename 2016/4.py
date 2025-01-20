from utils import *
inp = input_file(2016, 4).strip()

parsed_input = parser(inp, ["\n", r"-|\[|\]"])

real = lambda room: room[-2] * ("".join(sorted(lower, key=lambda l: -("".join(room[:-2]).count(l))))[:5] == room[-1])
p1 = sum(map(real, parsed_input))

for i in parsed_input:
    if "north" in "".join(lower[(lower.index(l) + i[-2]) % 26] if l != " " else l for l in " ".join(i[:-2])):
        i[-2]
        break
p2 = i[-2]

output(p1, p2)