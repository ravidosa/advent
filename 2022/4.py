from utils import *
inp = input_file(2022, 4).strip()

parsed_input = parser(inp, ["\n", ",", "-"])

contain = lambda r1, r2: r1[0] <= r2[0] and r1[1] >= r2[1]
p1 = sum(contain(r1, r2) or contain(r2, r1) for r1, r2 in parsed_input)

overlap = lambda r1, r2: r1[1] >= r2[0] and r1[0] <= r2[1]
p2 = sum(overlap(r1, r2) or overlap(r2, r1) for r1, r2 in parsed_input)

output(p1, p2)