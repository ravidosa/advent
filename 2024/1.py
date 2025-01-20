from utils import *
inp = input_file(2024, 1).strip()

parsed_input = parser(inp, ["\n| +"])

l1 = sorted(parsed_input[::2])
l2 = sorted(parsed_input[1::2])

p1 = sum(abs(a - b) for a in l1 for b in l2)

p2 = sum(a * l2.count(a) for a in l1)

output(p1, p2)