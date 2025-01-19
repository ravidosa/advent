from utils import *
inp = input_file(2024, 1).strip()

parsed_input = parser(inp, ["\n| +"])

l1 = sorted(parsed_input[::2])
l2 = sorted(parsed_input[1::2])

p1 = sum(map(lambda a, b: abs(a - b), l1, l2))

p2 = sum(map(lambda a: a * l2.count(a), l1))

output(p1, p2)