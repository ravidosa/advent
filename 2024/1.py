from utils import *
inp = input_file(2024, 1).strip().replace("\n", " ")

parsed_input = parser(inp, "{{li }}")

l1 = sorted(parsed_input[::2])
l2 = sorted(parsed_input[1::2])

p1 = sum(abs(a - b) for a, b in zip(l1, l2))

p2 = sum(a * l2.count(a) for a in l1)

output(p1, p2)