from utils import *
inp = input_file(2022, 4).strip()

parsed_input = parser(inp, "{{i}}-{{i}},{{i}}-{{i}}")

contain = lambda r1, r2: r1[0] <= r2[0] and r1[1] >= r2[1]
p1 = sum(contain(i[:2], i[2:]) or contain(i[2:], i[:2]) for i in parsed_input)

overlap = lambda r1, r2: r1[1] >= r2[0] and r1[0] <= r2[1]
p2 = sum(overlap(i[:2], i[2:]) or overlap(i[2:], i[:2]) for i in parsed_input)

output(p1, p2)