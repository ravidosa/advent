from utils import *
inp = input_file(2015, 16).strip()

parsed_input = parser(inp, "Sue {{i}}: {{s}}: {{i}}, {{s}}: {{i}}, {{s}}: {{i}}")

sue = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

for i in parsed_input:
    num, pairs = i[0], zip(i[1::2], i[2::2])
    if all(sue[p[0]] == p[1] for p in pairs):
        break
p1 = num

for i in parsed_input:
    num, pairs = i[0], zip(i[1::2], i[2::2])
    if all(sue[p[0]] < p[1] if p[0] in ["cats", "trees"] else sue[p[0]] > p[1] if p[0] in ["pomeranians", "goldfish"] else sue[p[0]] == p[1] for p in pairs):
        break
p2 = num

output(p1, p2)